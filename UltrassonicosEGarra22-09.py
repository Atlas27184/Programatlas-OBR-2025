from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#================================================#
hub = PrimeHub(broadcast_channel=2, observe_channels=[1])
lateral_esq = UltrasonicSensor(Port.C)
frontal = UltrasonicSensor(Port.A)
lateral_dir = UltrasonicSensor(Port.B)
garra_esq = Motor(Port.F, Direction.COUNTERCLOCKWISE)
garra_dir = Motor(Port.E)
porta = Motor(Port.D)
drive_base = DriveBase(garra_esq, garra_dir, wheel_diameter=230, axle_track=8)
#================================================#
# Velocidade dos motores (em "unidades" do Pybricks)
_10_porcento = 185
_20_porcento = 370
_30_porcento = 555
_40_porcento = 740
_50_porcento = 925
_60_porcento = 1110
_70_porcento = 1295
_80_porcento = 1480
_90_porcento = 1665
_100_porcento = 1850
#================================================#
frontal.lights.on(100)
# Sobe
drive_base.straight(1150)
# Joga pro lado direito
drive_base.turn(3000)
drive_base.turn(-3000)
drive_base.straight(-1150)
wait(2000)
# Sobe
drive_base.straight(1150)
# Joga pro lado esquerdo
drive_base.turn(-3000)
drive_base.turn(3000)
drive_base.straight(-1150)
wait(2000)
# Sobe
drive_base.straight(1150)
# Joga pro lado esquerdo
drive_base.turn(-3000)
drive_base.turn(3000)
drive_base.straight(-1150)
# Abre esquerda
porta.run_angle(-_20_porcento, 36)
wait(2000)
porta.run_angle(_20_porcento, 36)
# Abre direita
porta.run_angle(_20_porcento, 36)
wait(2000)
porta.run_angle(-_20_porcento, 36)

while True:
    if (frontal.distance() / 10) < 6:
        hub.ble.broadcast('obstaculo')
    
    if ((lateral_esq.distance() / 10) < 75) and ((lateral_dir.distance() / 10) < 75) and ((lateral_esq.distance() + lateral_dir.distance()) > 30):
        hub.ble.broadcast('resgate')

#================================================#