"""=================================
File: OlinWorldMap.py
Author: Susan Fox
Date: July, 2017

The purpose of this file/class is to combine together the code about the graph view of the map, and the more continuous
view of the map. This includes utilities for drawing the map, maybe even drawing the graph on the map eventually,
calculating straight-line distances, graph search for finding shortest paths in the map, and other tools related
to the map.

Localizer: getVertices(), getData, straightDist()  but all in one method could become part of new class
monteCarlo: has a bunch that should change
"""

import math
# import random

import cv2
import numpy as np
 
# from FoxQueue import PriorityQueue
# import Graphs
# from DataPaths import basePath, graphMapData, mapLineData, cellMapData
# from Particle import Particle
# import MapGraph


class WorldMap(object):


    def __init__(self):
        self.olinImage = None
        self.currentMapImg = self.olinImage
        self.mapLines = []
        self.scaledLines = []
        self.mapParams = {}
        (self.mapMinX, self.mapMinY) = (0, 0)
        (self.mapMaxX, self.mapMaxY) = (0, 0)
        (self.mapTotalXDim, self.mapTotalYDim) = (0, 0)
        (self.imageWidth, self.imageHeight) = (0, 0)
        self.mapScaleFactor = None
        self.pixelsPerMeter = 20

        self._readContinuousMap("olinNewMap.txt")
        self.cleanMapImage()

    # -------------------------------------------------------------------
    # These methods update and display the map and poses or particles on it

    def cleanMapImage(self, obstacles = False, cells = False, drawCellNum=False):
        """Set the current map image to be a clean copy of the original."""
        self.currentMapImg = self.olinImage.copy()
        # self.drawNodes()
        if obstacles:
            self.drawObstacles()
        if cells:
            self.drawCells(drawCellNum=drawCellNum)


    def displayMap(self, window = "Map Image"):
        """Make a copy of the original image, and display it."""
        cv2.imshow(window, self.currentMapImg)
        cv2.waitKey(20)


    # -------------------------------------------------------------------
    # These public methods access those features that should be accessed

    def getMapSize(self):
        """Returns a tuple of the width and height (x, y) of the map, in meters."""
        return self.mapTotalXDim, self.mapTotalYDim

    # -------------------------------------------------------------------
    # These public methods calculate angles and straightline distances.


    def calcAngle(self, pos1, pos2):
        """Input: two (x, y) locations, given either as graph nodes or a tuple giving an (x, y) coordinate in the map space.
        Returns the angle direction of the line between the two nodes. 0 being north and going clockwise around"""
        (n1x, n1y) = self._nodeToCoord(pos1)

        (n2x, n2y) = self._nodeToCoord(pos2)

        # translate node1 and node2 so that node1 is at origin
        t2x, t2y = n2x - n1x, n2y - n1y

        radianAngle = math.atan2(t2y, t2x)
        degAngle = math.degrees(radianAngle)

        if -180.0 <= degAngle <= 0:
            degAngle += 360
        # else:
        #    degAngle = 360 - degAngle
        return degAngle


    def _nodeToCoord(self,node):
        """
        :param node: number of the node
        :return: x and y coordinates of the node
        """
        if type(node) is int:
            n1x, n1y = self.getLocation(node)
            return n1x, n1y
        elif type(node) in [tuple, list]:
            (n1x, n1y) = node[0:2]    # the slicing allows for poses as well as locations, ignores the angle
            return n1x, n1y
        else:  # bad data for node
            print("ERROR in WorldMap: Data cannot be converted to (x, y) location:", node, type(node))
            return None


    def straightDist2d(self, node1, node2):
        """For estimating the straightline distance between two (x,y) coordinates given either as a graph
        node or as locations. """
        (x1, y1) = self._nodeToCoord(node1)
        (x2, y2) = self._nodeToCoord(node2)
        return math.hypot(x1 - x2, y1 - y2)


    def straightDist3d(self, pose1, pose2):
        """This must take in two poses (x, y, h) triples, as tuples, and it computes a "straight-line" distance
        using the Euclidean distance for the first two and scaling the difference in heading to match."""
        (x1, y1, h1) = pose1
        (x2, y2, h2) = pose2
        hDiff = abs(h2 - h1)
        if hDiff > 180.0:
            hDiff = 360 - hDiff       # TODO: IS THIS RIGHT?
        hDiff = hDiff * (50/180.0)    # Scale heading difference
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + hDiff ** 2)


    # -------------------------------------------------------------------
    # Other calculations

    def isAllowedLocation(self, pose):
        """This takes a tuple containing 2 or 3 values and checks to see if it is valid by comparing it to the
        obstacles that are stored."""
        x = pose[0]
        y = pose[1]
        if x > self.mapMaxX or x < self.mapMinX or y > self.mapMaxY or y < self.mapMinY:
            return False
        return True


    # -------------------------------------------------------------------
    # The following methods read in the continuous map data file and make an image representation of the map
    def _readContinuousMap(self, filename):
        """Takes in a filename containing map information, and the number of pixels per meter in the final image,
        and it reads in the data from the file, and creates an image of the map accordingly."""
        params, lines = self._inputMap(filename)
        self.mapLines = lines
        self.mapParams = params
        self._setupContMapParameters()
        self._drawMap()


    def _inputMap(self, filename):
        """Given a filename, it reads in the data about the map from the file, returning the parameters of the map
        and a list of the lines specified in it."""
        fil = open(filename, 'r')
        parameters = self._readHeader(fil)
        lineList = self._readLines(fil)
        fil.close()
        return parameters, lineList


    def _readHeader(self, fil):
        """Read in the header information, which includes the size of the map, its scale, and
        how many lines make up its walls."""
        # Loop until you see the LINES line
        params = dict()
        while True:
            nextLine = fil.readline()
            nextLine = nextLine.strip()
            # If reach the end of the header section, stop
            if nextLine == "LINES" or nextLine == "":
                break
            lineWords = nextLine.split()
            if lineWords[0] == "LineMinPos:":
                params["minPos"] = [int(v) for v in lineWords[1:]]
            elif lineWords[0] == "LineMaxPos:":
                params["maxPos"] = [int(v) for v in lineWords[1:]]
            elif lineWords[0] == "NumLines:":
                params["numLines"] = [int(v) for v in lineWords[1:]]
            elif lineWords[0] == "Scale:":
                params["scale"] = int(lineWords[1])
        return params


    def _readLines(self, fil):
        """Read in the lines, making a list of them. Each line is defined by four values, forming
        two points, which are the endpoints of the line."""
        lines = []
        biggestY = 0
        biggestX = 0
        while True:
            nextText = fil.readline()
            nextText = nextText.strip()
            # If read the end of the lines, stop
            if nextText == "DATA" or nextText == "":
                break
            elif nextText[0] == '#':  # line is a comment, skip it
                continue
            else:
                nextLine = [int(v) for v in nextText.split()]
                if nextLine[0] > biggestX:
                    biggestX = nextLine[0]
                if nextLine[2] > biggestX:
                    biggestX = nextLine[2]
                if nextLine[1] > biggestY:
                    biggestY = nextLine[1]
                if nextLine[3] > biggestY:
                    biggestY = nextLine[3]
                lines.append(nextLine)
        return lines


    def _setupContMapParameters(self):
        """Computes the map's size in meters based on the given scale."""
        self.mapScaleFactor = self.mapParams['scale']
        [minX, minY] = self.mapParams["minPos"]
        [maxX, maxY] = self.mapParams["maxPos"]
        self.mapMinX = self._scaleRawToMeters(minX)
        self.mapMinY = self._scaleRawToMeters(minY)
        self.mapMaxX = self._scaleRawToMeters(maxX)
        self.mapMaxY = self._scaleRawToMeters(maxY)

        self.mapTotalXDim = self._scaleRawToMeters(maxX - minX + 1)
        self.mapTotalYDim = self._scaleRawToMeters(maxY - minY + 1)

        self.imageHeight = self._scaleMetersToPixels(self.mapTotalXDim)
        self.imageWidth = self._scaleMetersToPixels(self.mapTotalYDim)


    def _drawMap(self):
        """This should use the parameters from the map to make a picture of the map.
         Draws the grid first, then the lines, and returns the new map image fo"""
        self.olinImage = 255 * np.ones((self.imageHeight, self.imageWidth, 3), np.uint8)
        self._drawGrid()

        lineColor = (0, 0, 0)
        i = 0
        for line in self.mapLines:
            scaledLine = [self._scaleRawToMeters(val) for val in line]
            # if (10 <= scaledLine[0] < 19) and (37 <= scaledLine[1] <= 39):
            #     print("Line:", line, scaledLine)
            #     lineColor = (0, 0, 255)
            # else:
            #     lineColor = (0, 0, 0)
            self.scaledLines.append(scaledLine)
            pt1 = scaledLine[0:2]
            pt2 = scaledLine[2:4]
            pixPt1 = self._convertWorldToPixels(pt1)
            pixPt2 = self._convertWorldToPixels(pt2)
            cv2.line(self.olinImage, pixPt1, pixPt2, lineColor, 1)
            i += 1



    def _drawGrid(self):
        """Draw horizontal and vertical lines marking each square meter on the picture."""
        # First, horizontal lines
        for x in range(0, int(self.mapTotalXDim)):
            lineCol = self._setLineColor(x)
            pt1 = self._convertWorldToPixels((x, 0.0))
            pt2 = self._convertWorldToPixels((x, self.mapTotalYDim))
            cv2.line(self.olinImage, pt1, pt2, lineCol)
            if x%5 == 0:
                cv2.putText(self.olinImage,str(x),self._convertWorldToPixels((x,1)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,128,0),2)
        # Next, vertical lines
        for y in range(0, int(self.mapTotalYDim)):
            lineCol = self._setLineColor(y)
            pt1 = self._convertWorldToPixels((0.0, y))
            pt2 = self._convertWorldToPixels((self.mapTotalXDim, y))
            cv2.line(self.olinImage, pt1, pt2, lineCol)
            if y%5 == 0:
                cv2.putText(self.olinImage,str(y),self._convertWorldToPixels((0.2,y)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,128,0),2)

        cv2.line(self.olinImage,self._convertWorldToPixels((45,15)),self._convertWorldToPixels((55,15)),(0,0,255))
        cv2.line(self.olinImage, self._convertWorldToPixels((50, 10)), self._convertWorldToPixels((50, 20)),(0, 0, 255))
        cv2.putText(self.olinImage,'0', self._convertWorldToPixels((56,15.5)),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
        cv2.putText(self.olinImage, '180', self._convertWorldToPixels((43, 16)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
        cv2.putText(self.olinImage, '90', self._convertWorldToPixels((49.5, 23)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
        cv2.putText(self.olinImage, '270', self._convertWorldToPixels((49.5, 9)), cv2.FONT_HERSHEY_SIMPLEX, 2,(0, 0, 255))


    def _setLineColor(self, value):
        """Chooses a line color based on what value is, black for 0, cyan for most others,
        and dark cyan for every 5."""
        if value == 0:
            return (0, 0, 0)
        elif value % 5 == 0:
            return (255, 255, 0)
        else:
            return (200, 200, 200)


    # -------------------------------------------------------------------
    # The following methods convert from the data file's representation to meters, and from meters to pixels and vice
    # versa, handling the fact that (0, 0) in pixels is in the upper left of the map image, and (0, 0) in meters is
    # at the lower right covern of the map image

    def _scaleRawToMeters(self, distance):
        """Convert the distance in mapfile units into meters using the given scale."""
        return distance / float(self.mapParams['scale'])


    def _scaleMetersToPixels(self, distance):
        """Convert the distance in meters into pixels using the pre-defined scale"""
        return int(distance * self.pixelsPerMeter)




    def _convertPixelsToWorld(self, mapPos):  #  (mapX, mapY)):
        """Converts coordinates in pixels, on the map, to coordinates (real-valued) in
        meters. Note that this also has to adjust for the rotation and flipping of the map."""
        # First flip x and y values around...
        mapX, mapY = mapPos
        flipY = self.mapTotalXDim - 1 - mapX
        flipX = self.mapTotalYDim - 1 - mapY
        # Next convert to meters from pixels, assuming 20 pixels per meter
        mapXMeters = flipX / 20.0
        mapYMeters = flipY / 20.0
        return (mapXMeters, mapYMeters)


    def _convertWorldToPixels(self, pos):  # (worldX, worldY)):
        """Converts coordinates in meters in the world to integer coordinates on the map
        Note that this also has to adjust for the rotation and flipping of the map."""
        # First convert from meters to pixels, assuming 20 pixels per meter
        worldX, worldY = pos
        pixelX = worldX * 20.0 #originally 20
        pixelY = worldY * 20.0
        # Next flip x and y values around
        mapX = self.imageWidth - 1 - pixelY
        mapY = self.imageHeight - 1 - pixelX
        return (int(mapX), int(mapY))




if __name__ == '__main__':
    mapper = WorldMap()
    mapper.cleanMapImage()

    mapper.displayMap()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

