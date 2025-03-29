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

def rotslow2(angle):
    arm2.run_angle(60, angle)

def rot2(angle):
    """Turn arm2 by realtive angle. Negative angle turns counterclockwise"""
    arm2.run_angle(500, angle)

def rot1stalled(speed, duty_limit = 40):
    arm1.run_until_stalled(speed, duty_limit=duty_limit)

 
def rot2stalled(speed, duty_limit = 40):
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

def stop():
    robot.stop()
    arm1.stop()
    arm2.stop()

def ship():
    """Forschungsschiff"""
    straight(930)
    """"Krabbenturm"""
    rot2stalled(200)
    wait(50)
    speed(300, 300, 900, 900)
    straight(-170)
    wait(250)
    speed(900, 900, 900, 900)
    rot2(-75)
    straight(-120)
    """"Dreizack"""
    turn(-90)
    straight(140)
    turn(51)
    straight(110)
    rot1(-90)
    wait(100)
    speed(900,1100,900,900)
    straight(-250)
    rot1(90)
    turn(38)
    straight(240)
    rot2stalled(400)
    straight(-220)
    rot2stalled(-600)
    straight(-500)
    stop()

def shark_and_circle_and_squid():
    # haifisch in seine heimat bringen
    arm1.reset_angle(0)
    arm2.reset_angle(0)
    straight(200)
    turn(-17)
    straight(530)
    # abenteuerreise zu den anderen aufgaben
    straight(-250)
    turn(-95)
    straight(380)
    turn(83)
    straight(300)
    turn(22)
    straight(490)
    # sonarentdeckung kreisding
    turn(-21)
    rot2stalled(300)
    rot2(-10)
    speed(100, 100, 100, 100)
    turn(-13)
    speed(900, 1100, 900, 900)
    rot2stalled(-400)
    # uboot zu gegner
    turn(-50)
    straight(-200)
    rot1(-95)
    speed(900,1100,900,900)
    straight(150)
    speed(500,1100,300,800)
    straight(-160)
    stop()

    
def mast():
    # Mast
    straight(200)
    turn(90)
    straight(195)
    turn(-86)
    rot2stalled(200)
    straight(105)
    rotspeed2(-93)
    # Grünes Komisches Ding (war sophias idee)
    turn(-27)
    straight(390)
    turn(38.5)
    straight(35)
    rot2stalled(600)
    rot2stalled(-200)
    # Ein Haifisch fiel in den Fluss in Lego City
    turn(-58)
    rot2stalled(-400) # Falls Arm vorher steckengeblieben ist
    straight(70)
    rot1stalled(-700, 50)
    # Taucher*in rausholen
    straight(-105)
    rot1stalled(300)
    turn(-35)
    rot2(56)
    wait(1200)
    DriveBase.reset(robot, 0, 0)
    straight(90)
    wait(50)
    speed(30, 30, 30, 30)
    rotslow2(-56)
    speed(900, 1100, 900, 900)
    # Mast aufstellen
    straight(-120)
    turn(165)
    rot2(60)
    straight(-100)
    rot2(-60)
    # Korallenbaum rausziehen
    turn(81)
    straight(190)
    turn(110)
    straight(-5)
    rot2stalled(200)
    turn(-60)
    rot2stalled(-200)
    straight(350)
    stop()


def korallenbaum():
    rot1(-90)
    wait(2000)
    straight(415)
    rot1(-65)
    straight(-100)
    rot1(65)
    straight(-210)
    # Taucher aufhängen
    wait(2000)
    turn(26.5)
    straight(755)
    rot1(-30)
    straight(-800)
    stop()

def taucher():
    rot1(-90)
    wait(2000)
    straight(600)
    turn(32)
    straight(190)
    rot1(-25)
    straight(-200)
    turn(-30)
    straight(-560)
    stop()

def boot_Kraken():
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
    straight(170)
    straight(-520)
    stop()


def Waal_Bodenprobe():
    demo()
    """Waal"""
    straight(400)
    turn(-45)
    straight(400)
    turn(40)
    straight(35)
    rot2stalled(400,40)
    straight(-70)
    """Bodenprobe"""
    rot2stalled(-400,40)
    turn(70)
    straight(112)
    rot2stalled(400,40)
    straight(-50)
    turn(-70)
    rot2stalled(-400,40)
    turn(-20)
    straight(-650)
    stop()

def uboot_Angler_BodenProbe_Korallen():
    demo()
    """uboot"""
    straight(400)
    turn(-47)
    straight(300)
    rot1(-104)
    """bei uns 435 auf den wert anpassen"""
    straight(415)
    """standart 0"""
    straight(-20)
    wait(900)
    """Angler"""
    straight(-85)
    rot1stalled(400, 40)
    turn(-100)
    straight(300)
    turn(110)
    straight(-170)
    speed(300,300,300,300)
    rot1stalled(-400, 40)
    turn(-15)
    straight(210)
    turn(-20)
    speed(900,1100,900,900)
    """Bodenprobe"""
    turn(50)
    straight(210)
    rot1(40)
    straight(40)
    turn(30)
    """Korallen"""
    rot1stalled(400, 40)
    turn(85)
    straight(-840)
    rot1stalled(400, 40)
    """zurück fahren"""
    straight(100)
    turn(100)
    straight(600)
    stop()

def main():

    while True:
    # Make a menu to choose a letter. You can also use numbers.
        selected = hub_menu("A", "B", "C","1","2","3","4","5")

    # Based on the selection, run a program.
        if selected == "A":
            boot_Kraken()
        elif selected == "B":
            Waal_Bodenprobe()
        elif selected == "C":
            uboot_Angler_BodenProbe_Korallen()
        elif selected == "1":
            demo()
            mast()
        elif selected == "2":
            demo()
            ship()
        elif selected == "3":
            demo()
            korallenbaum()
        elif selected == "4":
            demo()
            taucher()
        elif selected == "5":
            demo()
            shark_and_circle_and_squid()
        
        

main()
