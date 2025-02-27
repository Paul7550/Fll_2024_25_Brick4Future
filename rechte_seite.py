# (c) robotics team, IT department, HTL Hollabrunn
# pylint: disable=import-error, global-statement, invalid-name
"""
This is for pybricks, not the lego spike prime app!
Installation: https://code.pybricks.com/ -> On the left side: Install pybricks firmware
Reference manual: https://docs.pybricks.com/en/stable/
Tutorial: https://damom73.github.io/lego-spike-tutorials/index.html
"""
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

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
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.B, Direction.CLOCKWISE)
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

def rot2(angle):
    """Turn arm2 by realtive angle. Negative angle turns counterclockwise"""
    arm2.run_angle(500, angle)


def right_side():
    """Kraken im Korb"""
    straight(200)
    turn(-43)
    rot1(-30)
    straight(400)
    rot1(30)
    straight(-200)
    """wale umdrehen"""
    turn(35)
    straight(400)
    turn(-10)
    straight(30)
    rot2(80)
    straight(-70)
    rot2(-90)
    straight(-20)
    """" Wasserprobe"""
    turn(80)
    straight(17)
    rot2(100)
    wait(500)
    straight(-100)
    turn(-40)
    rot2(-90)
    """fahren zu gegner u-boot"""
    straight(40)
    turn(-70)
    straight(250)
    rot2(65)
    turn(-10)
    straight(40)
    rot2(-35)
    wait(1000)
    rot2(40)
    straight(-50)
    rot2(-70)
    """glowing fish"""
    turn(-90)
    straight(220)
    turn(80)
    rot1(-140)
    straight(180)
    """Boden Probe"""
    turn(55)
    rot1(42)
    straight(180)
    rot1(80)
    turn(-150)
    rot1(-130)
    turn(70)



# INIT
init()
speed(900,1100,300,1100)

# MAINLOOP
right_side()

