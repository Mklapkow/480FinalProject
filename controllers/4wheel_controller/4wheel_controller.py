from controller import Robot
import math
import routeFinding as rf

def findBearing():
    """
    Calculate the bearing angle from due north given compass 
    values.
    """
    north = compass.getValues()  
    rad = math.atan2(north[0], north[1])
    bearing = (rad - 1.5708) / math.pi * 180
    if bearing < 0.0:
        bearing = bearing + 360.0
    return bearing

def findCoord():
    """
    Returns the current position of the robot in (x,y,z) form.
    """
    return gps.getValues()

def angleBetweenTwoPoints(curr, target):
    """
    Finds the angle of rotation given 2 points with
    respect to the horizontal axis.
    """
    radianAngle = math.atan2(curr[1] - target[1], curr[0] - target[0])
    degreeAngle = math.degrees(radianAngle) + 90
    if degreeAngle < 0.0:
        degreeAngle = degreeAngle + 360.0
    return degreeAngle

def moveToNextNode(turnAngle, target):
    """
    Changes the speed of the robot given the necessary angle
    of forward progression to either turn, stop, or move the robot forward.
    """
    if turnAngle >= 2.5:
        leftSpeed = 3.0
        rightSpeed = -3.0
    elif turnAngle <= -2.5:
        leftSpeed = -3.0
        rightSpeed = 3.0
    elif abs(gps.getValues()[0] - target[0]) >= 0.5 or abs(gps.getValues()[1] - target[1]) >= 0.5:
        leftSpeed = 7.0
        rightSpeed = 7.0
    else:
        leftSpeed = 0
        rightSpeed = 0
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)


def nearestNode(curr):
    """
    Finds the nearest node given the robots current position.
    """
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
    """
    Moves the robot to the closest node.
    """
    curr = findCoord()
    firstNode = nearestNode(curr)
    target = rf.dictOfNodes.get(firstNode)
    distance = math.sqrt((curr[0] - target[0])**2 + (curr[1] - target[1])**2)
    count = 0
    while count * MOVEMENT_STEP <= distance :
        robot.step(TIME_STEP)
        count += 1
        newBearing = findBearing()
        curr = (curr[0] + count * MOVEMENT_STEP * math.cos(newBearing), curr[1] - count * 0.041117216 * math.sin(newBearing))
        print(newBearing)
        degreeAngle = angleBetweenTwoPoints(curr, target)
    
        turnAngle = newBearing - degreeAngle

        moveToNextNode(turnAngle, target)
        
    
    followPath(firstNode, goal)

def followPath(firstNode, goal):
    """
    Finds the path to the goal node given the initial node 
    the robot finds and the goal node. 
    """
    path = rf.pathFinder(firstNode, goal)
    for target in path[1]:
        if target != rf.dictOfNodes.get(firstNode):
            curr = findCoord()
            distance = math.sqrt((curr[0] - target[0])**2 + (curr[1] - target[1])**2)
            count = 0
            while count * MOVEMENT_STEP <= distance :
                robot.step(TIME_STEP)
                count += 1
                newBearing = findBearing()
                curr = (curr[0] + count * MOVEMENT_STEP * math.cos(newBearing), curr[1] - count * 0.041117216 * math.sin(newBearing))
                print(newBearing)
                degreeAngle = angleBetweenTwoPoints(curr, target)
            
                turnAngle = newBearing - degreeAngle
    
                moveToNextNode(turnAngle, target)
        leftSpeed = 0
        rightSpeed = 0
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(rightSpeed)
        wheels[2].setVelocity(leftSpeed)
        wheels[3].setVelocity(rightSpeed)
    print("Not lost anymore!")
    
      
            
        

if __name__=="__main__":
    TIME_STEP = 32
    MOVEMENT_STEP = 0.041117216
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
    goal = "room_260"
    firstNode = firstMove(goal)

