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

def mover_dois(velocidade_1, velocidade_2, tempo):
    garra_esq.run(velocidade_1)
    garra_dir.run(velocidade_2)
    wait(tempo)
    garra_esq.hold()
    garra_dir.hold()
resgate = 0
#================================================#
while True:
    data = hub.ble.observe(1)
    if data != None:
        if data == 'Resgate':
            resgate = 1
            mover_dois(-1000, -1000, 1300) # Volta muito
            mover_dois(800, 800, 350) # Um pouco pra frente
            mover_dois(600, 600, 400) # Mais um pouco pra frente
            mover_dois(-600, -600, 400) # Recalibra
            continue
        if data == "Saiu":
            resgate = 0
        if data == "CadeSaida":
            if (frontal.distance() / 10) > 110:
                print("Frente")
                hub.ble.broadcast("SaidaFrente")
                wait(1000)
            elif (lateral_esq.distance() / 10) > 110:
                print("Esquerda")
                hub.ble.broadcast("SaidaEsquerda")
                wait(1000)
            elif (lateral_dir.distance() / 10) > 110:
                print("Direita")
                hub.ble.broadcast("SaidaDireita")
                wait(1000)
            else:
                print("NaoTem")
                hub.ble.broadcast("NaoTem")
                wait(1000)
        if data == "Saida":
            saida = 1
            continue
        
        if data == "TemSaida?":
            while not (frontal.distance() / 10) > 90:
                wait(1)
            print("Disnara")
            hub.ble.broadcast("TemSaida")
            print("Mandei a Disnara")
            wait(1000)
            hub.ble.broadcast("ProcuraDenovo")
        
            if resgate == 1 and (frontal.distance() / 10) < 10:
                hub.ble.broadcast("TentaDenovo")

        if data == f'AlarmeFalso':
            resgate = 0
            wait(500)
            continue
        if data == 'viva':
            # JOGAR DIREITA
            mover_dois(600, 600, 700) # Pega a bolinha
            wait(1750) # Espera a ré
            mover_dois(600, 600, 1200) # Termina de subir
            mover_dois(600, -600, 500) # Joga pra direita
            mover_dois(-1000, -1000, 1300) # Volta muito
            mover_dois(800, 800, 350) # Um pouco pra frente
            mover_dois(600, 600, 400) # Mais um pouco pra frente
            mover_dois(-600, -600, 400) # Recalibra
            continue
        elif data == 'morta':
            # JOGAR ESQUERDA
            mover_dois(600, 600, 700) # Pega a bolinha
            wait(1750) # Espera a ré
            mover_dois(600, 600, 1200) # Termina de subir
            mover_dois(-600, 600, 500) # Joga pra esquerda
            mover_dois(-1000, -1000, 1300) # Volta muito
            mover_dois(800, 800, 350) # Um pouco pra frente
            mover_dois(600, 600, 400) # Mais um pouco pra frente
            mover_dois(-600, -600, 400) # Recalibra
            continue
        elif data == "Direita":
            print("DIREITA")
            hub.speaker.beep()
            # Abre esquerda
            porta.run(-_40_porcento)
            wait(1000)
            porta.brake()
            wait(1000)
        elif data == "Esquerda":
            print("ESQUERDA")
            hub.speaker.beep()
            # Abre direita
            porta.run(_40_porcento)
            wait(1000)
            porta.brake()
            wait(1000)
        elif data == "para":
            continue

    if (frontal.distance() / 10) < 10 and resgate != 1:
        hub.ble.broadcast('obstaculo')
        print('obstaculo')

#================================================#