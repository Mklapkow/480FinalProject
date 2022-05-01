"""drive_my_robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Lidar
import math

robot = Robot()
TIME_STEP = 64
nodes = []
 
#Initialize robot parts
ds = []
dsNames = ['lidar', 'gps', 'compass']
for i in range(3):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
        
lidar = ds[0]
lidar.enablePointCloud()
    
gps = ds[1]

compass = ds[2]
    
wheels = []
wheelsNames = ['motor_1', 'motor_2']
for i in range(2):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
       
       
#Find closest note 
    # LeftObstacleCounter = 0
    # RightObstacleCounter = 0
robot.step(TIME_STEP)
curr = gps.getValues()
north = compass.getValues()
print(curr) 
print(north)  

#calculate bearing
rad = math.atan2(north[0], north[1])
bearing = (rad - 1.5708) / math.pi * 180
if bearing < 0.0:
    bearing = bearing + 360.0

print(bearing)



# for node in nodes:
    # distance = ((((curr[0] - node.getCoords()[0])**2) + ((curr[1]-node.getCoords()[1])**2))) )**0.5)
    # if distance < shortest_distance or shortest_distance is None:
        # shortest_distance = distance
        # shortest_distance_coords = node.getCoords()
        

# dx = abs(shortest_distance_coords[0] - curr[0])
# dy = abs(shortest_distance_coords[1] - curr[1])
# angle_rad = math.atan2(dy, dx)
# angle_deg = (angle_rad - 1.5708) / math.pi * 180

#NEXT TURN ROBOT TOWARDS THIS ANGLE USING CURRENT ANGLE

leftSpeed = 5.0
rightSpeed = 5.0
wheels[0].setVelocity(leftSpeed)
wheels[1].setVelocity(rightSpeed)
    
while robot.step(TIME_STEP) != -1:
    
    north = compass.getValues()
    
   
    rad = math.atan2(north[0], north[1])
    bearing = (rad - 1.5708) / math.pi * 180
    if bearing < 0.0:
        bearing = bearing + 360.0
    
    print(bearing)
 

      
        
 
            
                
        
   