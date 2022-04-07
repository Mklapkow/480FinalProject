"""drive_my_robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,DistanceSensor

TIME_STEP = 64
robot = Robot()

ds = []
dsNames = ['sensor_1', 'sensor_2']
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
wheels = []
wheelsNames = ['motor_1', 'motor_2']
for i in range(2):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
    
LeftObstacleCounter = 0
RightObstacleCounter = 0

while robot.step(TIME_STEP) != -1:

    leftSpeed = 5.0
    rightSpeed = 5.0
    
    if LeftObstacleCounter > 0:
        leftSpeed = -5.0
        rightSpeed = 5.0
        LeftObstacleCounter -= 10
    elif RightObstacleCounter > 0:
        leftSpeed = -5.0
        rightSpeed = 5.0
        RightObstacleCounter -= 10
    else:  # read sensors 
        if ds[0].getValue() < 950.0:
            LeftObstacleCounter = 100
        elif ds[1].getValue() < 950.0:
            RightObstacleCounter = 100
            
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
  
        
        
            
    
    # Enter here exit cleanup code.
