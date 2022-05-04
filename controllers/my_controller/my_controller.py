from controller import Robot
import Graphs

TIME_STEP = 64
robot = Robot()
wheels = []
wheelsNames = ['motor_1', 'motor_2', 'motor_3', 'motor_4']

if __name__=="__main__":
    for i in range(4):
        wheels.append(robot.getDevice(wheelsNames[i]))
        wheels[i].setPosition(float('inf'))
        wheels[i].setVelocity(0.0)

    while robot.step(TIME_STEP) != -1:
        leftSpeed = 10.0
        rightSpeed = 10.0

        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(rightSpeed)
        wheels[2].setVelocity(leftSpeed)
        wheels[3].setVelocity(rightSpeed)







