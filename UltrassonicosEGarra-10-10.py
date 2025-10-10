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
_10_porcento = 100
_20_porcento = 200
_30_porcento = 300
_40_porcento = 400
_50_porcento = 500
_60_porcento = 600
_70_porcento = 700
_80_porcento = 800
_90_porcento = 900
_100_porcento = 1000
#================================================#
'''frontal.lights.on(100)
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
'''
resgate = 0
while True:
    data = hub.ble.observe(1)
    if data != None:
        print('Recebeu')
        if data == 'viva':
            print('Viva')
            # Sobe
            drive_base.straight(1250)
            # Joga pro lado direito
            drive_base.turn(5000)
            drive_base.turn(-5000)
            drive_base.straight(-1250)
            wait(2000)
            print("pegou")
            continue
        elif data == 'morta':
            print('Morta')
            drive_base.straight(1250)
            # Joga pro lado esquerdo
            drive_base.turn(-5000)
            drive_base.turn(5000)
            drive_base.straight(-1250)
            wait(2000)
            print("pegou")
            continue
        elif data == "AbreMorta":
            # Abre esquerda
            porta.run_angle(-_20_porcento, 36)
            wait(4000)
        elif data == "FechaMorta":
            porta.run_angle(_20_porcento, 36)
        elif data == "AbreViva":
            # Abre direita
            porta.run_angle(_20_porcento, 36)
            wait(4000)
        elif data == "FechaViva":
            porta.run_angle(-_20_porcento, 36)
        elif data == "para":
            continue
    
    if (frontal.distance() / 10) < 10 and resgate != 0:
        hub.ble.broadcast('obstaculo')
        print('obstaculo')
        
    if ((lateral_esq.distance() / 10) < 75) and ((lateral_dir.distance() / 10) < 75) and ((lateral_esq.distance() + lateral_dir.distance()) > 30):
        hub.ble.broadcast('resgate')
#================================================#