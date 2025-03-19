# (c) robotics team, IT department, HTL Hollabrunn
# pylint: disable=import-error, global-statement, invalid-name
"""
This is for pybricks, not the lego spike prime app!
Installation: https://code.pybricks.com/ -> On the left side: Install pybricks firmware
Reference manual: https://docs.pybricks.com/en/stable/
Tutorial: https://damom73.github.io/lego-spike-tutorials/index.html
"""
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
from pybricks.parameters import Axis, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.tools import hub_menu
from pybricks.iodevices import XboxController

xbox = XboxController
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

def rot1stalled(speed, duty_limit):
    arm1.run_until_stalled(speed, duty_limit=duty_limit)

 
def rot2stalled(speed, duty_limit):
    arm2.run_until_stalled(speed, duty_limit=duty_limit)


def rotspeed2(angle):
    arm2.run_angle(1000, angle)    
    
def main():
    joystick_left()
init()
speed(900,1100,900,900)

def demo():
    rot1stalled(500, 40)
    rot2stalled(-200, 50)

def boot():
    straight(20)
    turn(-30)
    straight(300)
    turn(70)
    straight(210)
    rot2(-80)
    turn(30)
    straight(-150)
    turn(-120)
    straight(-60)
    rot2(-70)
    straight(150)
    straight(-500)

def kraken_Waal_Bodenprobe():
    demo()
    """Kraken"""
    straight(230)
    turn(-47)
    rot1(-50)
    straight(350)
    straight(-100)
    """Waal"""
    rot1(50)
    turn(45)
    straight(350)
    turn(-25)
    rot2(100)
    speed(300,1100,900,900)
    straight(-90)
    rot2(-100)
    """Boden Probe"""
    turn(87)
    speed(300,300,300,300)
    rot2(90)
    straight(-80)
    speed(900,1100,900,900)
    turn(-40)
    rot2stalled(-400, 50)
    turn(-40)
    straight(-600)
def uboot_Angler_BodenProbe_Korallen():
    demo()
    """uboot"""
    straight(400)
    turn(-47)
    straight(300)
    rot1(-104)
    """bei uns 435 auf den wert anpassen"""
    straight(435)
    """standart 0"""
    straight(-0)
    wait(900)
    """Angler"""
    straight(-85)
    rot1stalled(400, 40)
    turn(-100)
    straight(290)
    turn(100)
    straight(-170)
    speed(300,300,300,300)
    rot1stalled(-400, 40)
    turn(-13)
    straight(200)
    turn(-20)
    """Bodenprobe"""
    turn(48)
    rot1stalled(400,40)
    rot2(70)
    straight(280)
    rot2(-70)
    straight(-60)
    """Korallen"""
    rot1stalled(400, 40)
    turn(119)
    speed(900,1100,900,900)
    straight(-840)
    rot1stalled(400, 40)
    """zurück fahren"""
    straight(100)
    turn(100)
    straight(600)
    

def main():
    uboot_Angler_BodenProbe_Korallen()
    #kraken_Waal_Bodenprobe()
    #boot()

main()