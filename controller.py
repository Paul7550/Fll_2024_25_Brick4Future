from pybricks.iodevices import XboxController
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Color, Direction, Port, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Set up all devices.

controller = XboxController()
hub = None
robot = None
arm1 = None
arm2 = None
def _init_hub():
    """Initialize the prime hub"""
    _hub = PrimeHub(top_side=Axis.Z,front_side=Axis.X)
    _hub.speaker.beep()
    _hub.light.on(Color.GREEN)
    return _hub

def _init_robot():
    """Initializes the drive base (aka robot)"""
    right_motor = Motor(Port.B, Direction.CLOCKWISE)
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    _robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=96)
    _robot.use_gyro(True)
    print(_robot.settings())
    return _robot

def _init_arm1():
    """Initializes the first arm"""
    arm = Motor(Port.E)
    return arm

def _init_arm2():
    """Initializes the second arm"""
    arm = Motor(Port.F)
    return arm

def init():
    """initialization function, should only be called once"""
    global hub, robot, arm1, arm2
    hub = _init_hub()
    robot = _init_robot()
    arm1 = _init_arm1()
    arm2 = _init_arm2()
    wait(10)

def speed(straight_speed, straight_acceleration, turn_rate, turn_acceleration):
    """Here you can modify the speed settings. You can call this function multiple times"""
    robot.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)

def straight(distance):
    """Drive straight. Use negative value to drive back"""
    robot.straight(distance)

def turn(angle):
    """Turn by relative angle. Negative angle turns counterclockwise"""
    robot.turn(angle)

def rot1(angle):
    """Turn arm1 by realtive angle. Negative angle turns counterclockwise"""
    arm1.run_angle(500, angle)

def rotspeed1(angle):
    arm1.run_angle(1000, angle)    

def rotslow1(angle):
    arm1.run_angle(420, angle)

def rot2(angle):
    """Turn arm2 by realtive angle. Negative angle turns counterclockwise"""
    arm2.run_angle(500, angle)
def rot1stalled(speed):
    arm1.run_until_stalled(speed, duty_limit=50)

 
def rot2stalled(speed):
    arm2.run_until_stalled(speed, duty_limit=50)


def rotspeed2(angle):
    arm2.run_angle(1000, angle)    

def drive(trigger):
    dir1 = getDir()
    speed = trigger * 5 * dir1
    robot.drive(speed, 0)

def turn_con():
    angle= controller.joystick_left()
    angle = angle[0]
    robot.drive(10, angle)

def rot_right():
    speed = controller.joystick_left()
    speed = speed[1]
    arm2.run(speed*4*-1)

def rot_left():
    speed = controller.joystick_left()
    speed = speed[1]
    arm1.run(speed*4)

def getDir():
    direc = controller.joystick_left()
    direc = direc [1] 
    if(direc >= 0):
        direc = 1
    if(direc < 0):
        direc = -1
    return direc
def arm1_stall():
    direc = getDir()
    rot1stalled(400 * direc)
    if(direc == 1):
        measurestalled1 = True
    elif(direc == -1):
        measurestalled1 = False 
def arm2_stall():
    direc = getDir()
    rot2stalled(400 * direc)
    if(direc == 1):
        measurestalled2 = True
    elif(direc == -1):
        measurestalled2 = False 
def resetAll():
    robot.reset()
    arm1.reset_angle()
    arm2.reset_angle()

# INIT
init()
speed(900,1100,300,1100)

# The main program starts here.
measureDis = False
measureRot = False
measureArm1 = False
measureArm2 = False
measurestalled1 = False 
measurestalled2 = False 
print("def record():")
while True:
    trigger= controller.triggers()
    rightTrigger = trigger[1]

    if(rightTrigger > 0):
        measureDis = True
        drive(rightTrigger)
    elif(Button.Y in controller.buttons.pressed()):
        measureRot = True
        turn_con()
    elif(Button.LB in controller.buttons.pressed()):
        measureArm1 = True
        rot_left()
    elif(Button.RB in controller.buttons.pressed()):
        measureArm2 = True
        rot_right()
    elif(Button.X in controller.buttons.pressed()):
        arm1_stall()
        if(measureArm1):
            print("    rot1stalled(400,40)")
        elif(not measureArm1):
            print("    rot1stalled(-400,40)")
    elif(Button.B in controller.buttons.pressed()):
        arm2_stall()
        if(measureArm2):
            print("    rot2stalled(400,40)")
        elif(not measureArm2):
            print("    rot2stalled(-400,40)")
    else:
        robot.stop()
        if(measureDis):
            print("    straight(",robot.distance(),")")
            measureDis = False
        if(measureRot):
            print("    turn(",robot.angle(),")")
            measureRot = False
        if(measureArm1):
            print("    rot1(", arm1.angle(),")")
            measureArm1 = False
        if(measureArm2):
            print("    rot2(", arm2.angle(),")")
            measureArm2 = False
        resetAll()