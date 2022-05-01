from controller import Robot
import math
import routeFinding as rf

def findBearing():
    north = compass.getValues()  
    rad = math.atan2(north[0], north[1])
    bearing = (rad - 1.5708) / math.pi * 180
    if bearing < 0.0:
        bearing = bearing + 360.0
    return bearing

def findCoord():
    return gps.getValues()

def angleBetweenTwoPoints(curr, target):
    radianAngle = math.atan2(curr[1] - target[1], curr[0] - target[0])
    degreeAngle = math.degrees(radianAngle) + 90
    if degreeAngle < 0.0:
        degreeAngle = degreeAngle + 360.0
    return degreeAngle

def moveToNextNode(turnAngle, target):
    if turnAngle >= 2.5:
        leftSpeed = -3.0
        rightSpeed = 3.0
    elif abs(gps.getValues()[0] - target[0]) >= 0.9 and abs(gps.getValues()[1] - target[1]) >= 0.9:
        leftSpeed = 5.0
        rightSpeed = 5.0
    else:
        leftSpeed = 0
        rightSpeed = 0
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)


def nearestNode(curr):
    dictOfNodes = rf.getNodes()
    nearest = 99999
    nearestName = None
    for i in dictOfNodes.keys():
        res = rf.calculateDistance(curr[0], curr[1], dictOfNodes.get(i)[0], dictOfNodes.get(i)[1])
        if res < nearest:
            nearest = res
            nearestName = i
    return nearestName

def firstMove(goal):
   
    curr = findCoord()
    firstNode = nearestNode(curr)
    target = rf.dictOfNodes.get(firstNode)

    while abs(gps.getValues()[0] - target[0]) > 1 and abs(gps.getValues()[1] - target[1]) > 1:
        robot.step(TIME_STEP)
        print('x: ' + str(abs(gps.getValues()[0] - target[0])))
        print('y: ' + str(abs(gps.getValues()[1] - target[1])))
        newBearing = findBearing()
        curr = findCoord()

        degreeAngle = angleBetweenTwoPoints(curr, target)
    
        turnAngle = abs(newBearing - degreeAngle)

        moveToNextNode(turnAngle, target)
        
    followPath(firstNode, goal)


def followPath(firstNode, goal):
    path = rf.pathFinder(firstNode, goal)
    print(path)
    for target in path[1]:
        while abs(gps.getValues()[0] - target[0]) > 1 and abs(gps.getValues()[1] - target[1]) > 1:
            robot.step(TIME_STEP)
            newBearing = findBearing()
            curr = findCoord()

            degreeAngle = angleBetweenTwoPoints(curr, target)
        
            turnAngle = abs(newBearing - degreeAngle)

            moveToNextNode(turnAngle, target)
    
      
            
        

if __name__=="__main__":
    TIME_STEP = 32
    robot = Robot()
    ds = []
    dsNames = ['ds_right', 'ds_left', 'gps', 'compass']
    for i in range(4):
        ds.append(robot.getDevice(dsNames[i]))
        ds[i].enable(TIME_STEP)
    wheels = []
    wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
    for i in range(4):
        wheels.append(robot.getDevice(wheelsNames[i]))
        wheels[i].setPosition(float('inf'))
        wheels[i].setVelocity(0.0)


    gps = ds[2]
    compass = ds[3]
    robot.step(TIME_STEP)
    goal = "room_281_01"
    firstNode = firstMove(goal)

