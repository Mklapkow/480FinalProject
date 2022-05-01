from controller import Robot
import math

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
avoidObstacleCounter = 0

gps = ds[2]
compass = ds[3]
robot.step(TIME_STEP)
curr = gps.getValues()
north = compass.getValues()
print(curr)   


rad = math.atan2(north[0], north[1])
bearing = (rad - 1.5708) / math.pi * 180
if bearing < 0.0:
    bearing = bearing + 360.0


while robot.step(TIME_STEP) != -1:
    target = (58, -16.3)
    # if avoidObstacleCounter > 0:
        # avoidObstacleCounter -= 1
        # leftSpeed = 1.0
        # rightSpeed = -1.0
    # else:  # read sensors
        # for i in range(2):
            # if ds[i].getValue() < 950.0:
                # avoidObstacleCounter = 100
    north = compass.getValues()            
    rad = math.atan2(north[0], north[1])
    newBearing = (rad - 1.5708) / math.pi * 180
    if newBearing < 0.0:
        newBearing = newBearing + 360.0
        
    radianAngle = math.atan2(curr[1] - target[1], curr[0] - target[0])
    degreeAngle = math.degrees(radianAngle) + 90
    if degreeAngle < 0.0:
        degreeAngle = degreeAngle + 360.0
   
    
    turnAngle = abs(newBearing - degreeAngle)
  
   
    if turnAngle >= 2:
        leftSpeed = -3.0
        rightSpeed = 3.0
    elif abs(gps.getValues()[0] - target[0]) >= 0.5 or abs(gps.getValues()[1] - target[1]) >= 0.5:
        leftSpeed = 5.0
        rightSpeed = 5.0
    else:
        leftSpeed = 0
        rightSpeed = 0
    
    

    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
