from controller import Robot
import math


def initializeRobot(self):
    self.TIME_STEP = 32
    self.robot = Robot()
    self.ds = []
    dsNames = ['ds_right', 'ds_left', 'gps', 'compass']
    for i in range(4):
        self.ds.append(self.robot.getDevice(dsNames[i]))
        self.ds[i].enable(self.TIME_STEP)
    wheels = []
    wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
    for i in range(4):
        wheels.append(self.robot.getDevice(wheelsNames[i]))
        wheels[i].setPosition(float('inf'))
        wheels[i].setVelocity(0.0)

avoidObstacleCounter = 0

def initLocal(self):

    self.gps = self.ds[2]
    self.compass = self.ds[3]
    self.robot.step(self.TIME_STEP)

def findBearing(self):
    self.north = self.compass.getValues()  
    rad = math.atan2(north[0], north[1])
    bearing = (rad - 1.5708) / math.pi * 180
    if bearing < 0.0:
        bearing = bearing + 360.0
    return bearing

def findCoord(self):
    return self.gps.getValues()

def angleBetweenTwoPoints(self, curr, target):
    radianAngle = math.atan2(curr[1] - target[1], curr[0] - target[0])
    degreeAngle = math.degrees(radianAngle) + 90
    if degreeAngle < 0.0:
        degreeAngle = degreeAngle + 360.0
    return degreeAngle

def moveToNextNode(self, turnAngle, target):
    if turnAngle >= 2:
        leftSpeed = -3.0
        rightSpeed = 3.0
    elif abs(self.gps.getValues()[0] - target[0]) >= 0.5 or abs(self.gps.getValues()[1] - target[1]) >= 0.5:
        leftSpeed = 5.0
        rightSpeed = 5.0
    else:
        leftSpeed = 0
        rightSpeed = 0
    self.wheels[0].setVelocity(leftSpeed)
    self.wheels[1].setVelocity(rightSpeed)
    self.wheels[2].setVelocity(leftSpeed)
    self.wheels[3].setVelocity(rightSpeed)
    

def run(self):
    while self.robot.step(self.TIME_STEP) != -1:
        target = (58, -16.3)
        # if avoidObstacleCounter > 0:
            # avoidObstacleCounter -= 1
            # leftSpeed = 1.0
            # rightSpeed = -1.0
        # else:  # read sensors
            # for i in range(2):
                # if ds[i].getValue() < 950.0:
                    # avoidObstacleCounter = 100


        newBearing = findBearing()
        curr = findCoord()
            
        degreeAngle = angleBetweenTwoPoints(curr, target)
        turnAngle = abs(newBearing - degreeAngle)

        moveToNextNode(turnAngle, target)


if __name__=="__main__":
    initializeRobot()

