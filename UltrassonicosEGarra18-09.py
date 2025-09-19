from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#================================================#
hub = PrimeHub(broadcast_channel=2, observe_channels=[1])
lateral_esq = UltrasonicSensor(Port.A)
frontal = UltrasonicSensor(Port.B)
lateral_dir = UltrasonicSensor(Port.C)
garra_esq = Motor(Port.D)
garra_dir = Motor(Port.E)
porta = Motor(Port.F)
#================================================#
while True:
    if (frontal.distance() / 10) < 6:
        hub.ble.broadcast('obstaculo')
    
    if ((lateral_esq.distance() / 10) < 75) and ((lateral_dir.distance() / 10) < 75) and ((lateral_esq.distance() + lateral_dir.distance()) > 30):
        hub.ble.broadcast('resgate') 
#================================================#