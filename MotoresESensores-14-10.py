from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port, Button
from pybricks.tools import wait, StopWatch, Matrix
from pybricks.robotics import DriveBase
from usys import stdin, stdout 
from uselect import poll
#================================================#

SQUARE_1 = Matrix(
    [
        [100, 100, 0, 0, 0],
        [100, 100, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)
SQUARE_2 = Matrix(
    [
        [0, 0, 0, 100, 100],
        [0, 0, 0, 100, 100],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)
Cara = Matrix(
    [
        [100, 100, 0, 100, 100],
        [100, 100, 0, 100, 100],
        [0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 100, 100, 0],
    ]
)
 
#================================================#
# Inicialização do hub e sensores/motores
hub = PrimeHub(broadcast_channel=1, observe_channels=[2, 3])
 
sensor_1 = ColorSensor(Port.B)
sensor_2 = ColorSensor(Port.A)
sensor_3 = ColorSensor(Port.C)
sensor_4 = ColorSensor(Port.D)

Color.GREEN = Color(h=160, s=80, v=20)
Color.WHITE = Color(h=200, s=20, v=60)
Color.BLACK = Color(h=200, s=20, v=15)
Color.RED = Color(h=350, s=90, v=45)

my_colors = (Color.GREEN, Color.WHITE, Color.BLACK, Color.RED)

sensor_1.detectable_colors(my_colors)
sensor_2.detectable_colors(my_colors)
sensor_3.detectable_colors(my_colors)
sensor_4.detectable_colors(my_colors)

motor_esquerdo = Motor(Port.F, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.E)
drive_base = DriveBase(motor_esquerdo, motor_direito, wheel_diameter=43.2, axle_track=80)
drive_base.settings(500, 750, 150, 750)
 
hub.imu.reset_heading(0)
cronometro = StopWatch()
cronometro.reset()
 
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
 
velocidade_padrão = 800
kP = 10
kD = 0.005
kPTurn = 3
lastTime = cronometro.time() / 1000
last_error = 0.0
estado = 4
resgate = 0
keyboard = poll()
keyboard.register(stdin)
wait(300)
stdout.buffer.write(b"dia")
#================================================#
# Funções auxiliares
def PararMotores():
    motor_esquerdo.hold()
    motor_direito.hold()
    
    pressed = hub.buttons.pressed()
    if Button.LEFT in pressed:
        hub.speaker.beep()
        estado = 5
        return
    if Button.RIGHT in pressed:
        hub.speaker.beep()
        estado = 1
        return
 
def DoisMotores(velocidade):
    drive_base.straight(velocidade)

def DoisMotoresGiroSemTempo(velocidade_esquerda, velocidade_direita):
    motor_esquerdo.run(velocidade_esquerda)
    motor_direito.run(velocidade_direita)
    
    pressed = hub.buttons.pressed()
    if Button.LEFT in pressed:
        hub.speaker.beep()
        estado = 5
        return
    if Button.RIGHT in pressed:
        hub.speaker.beep()
        estado = 1
        return
 
def DoisMotoresGiro(velocidade_esquerda, velocidade_direita, tempo):
    motor_esquerdo.run(velocidade_esquerda)
    motor_direito.run(velocidade_direita)
    
    pressed = hub.buttons.pressed()
    if Button.LEFT in pressed:
        hub.speaker.beep()
        estado = 5
        return
    if Button.RIGHT in pressed:
        hub.speaker.beep()
        estado = 1
        return

    wait(tempo)
    PararMotores()
 
def Giro90Esquerda():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação - 90) - hub.imu.heading()
    while not (Turn_Error < 1) or not (Turn_Error > -1):
        Turn_Error = (Orientação - 90) - hub.imu.heading()
        motor_esquerdo.run(((Turn_Error * -1) * kPTurn) * 10)
        motor_direito.run((Turn_Error * kPTurn) * 10)

        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            hub.speaker.beep()
            estado = 5
            return
        if Button.RIGHT in pressed:
            hub.speaker.beep()
            estado = 1
            return

        if (Turn_Error < 1) and (Turn_Error > -1):
            break
    PararMotores()
 
def Giro90Direita():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 90) - hub.imu.heading()
    while not (Turn_Error < 1) or not (Turn_Error > -1):
        Turn_Error = (Orientação + 90) - hub.imu.heading()
        motor_esquerdo.run(((Turn_Error * -1) * kPTurn) * 10)
        motor_direito.run((Turn_Error * kPTurn) * 10)

        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
            hub.speaker.beep()
            estado = 5
            return
        if Button.RIGHT in pressed:
            hub.speaker.beep()
            estado = 1
            return

        if (Turn_Error < 1) and (Turn_Error > -1):
            break
    PararMotores()
 
def Giro180Direita():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 180) - hub.imu.heading()
    while not (Turn_Error < 1) or not (Turn_Error > -1):
        Turn_Error = (Orientação + 180) - hub.imu.heading()
        motor_esquerdo.run(((Turn_Error * -1) * kPTurn) * 10)
        motor_direito.run((Turn_Error * kPTurn) * 10)
        
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            hub.speaker.beep()
            estado = 5
            return
        if Button.RIGHT in pressed:
            hub.speaker.beep()
            estado = 1
            return

        if (Turn_Error < 1) and (Turn_Error > -1):
            break
    PararMotores()

def Giro45Esquerda():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação - 45) - hub.imu.heading()
    while not (Turn_Error < 1) or not (Turn_Error > -1):
        Turn_Error = (Orientação - 45) - hub.imu.heading()
        motor_esquerdo.run(((Turn_Error * -1) * kPTurn) * 10)
        motor_direito.run((Turn_Error * kPTurn) * 10)

        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            hub.speaker.beep()
            estado = 5
            return
        if Button.RIGHT in pressed:
            hub.speaker.beep()
            estado = 1
            return

        if (Turn_Error < 1) and (Turn_Error > -1):
            break
    PararMotores()
 
def Giro45Direita():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 45) - hub.imu.heading()
    while not (Turn_Error < 1) or not (Turn_Error > -1):
        Turn_Error = (Orientação + 45) - hub.imu.heading()
        motor_esquerdo.run(((Turn_Error * -1) * kPTurn) * 10)
        motor_direito.run((Turn_Error * kPTurn) * 10)
        
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            hub.speaker.beep()
            estado = 5
            return
        if Button.RIGHT in pressed:
            hub.speaker.beep()
            estado = 1
            return

        if (Turn_Error < 1) and (Turn_Error > -1):
            break
    PararMotores()
 
def Girar180():
    DoisMotoresGiro(800, -800, 2500)
    while sensor_2.color() != Color.BLACK:
        motor_esquerdo.run(velocidade_padrão)
        motor_direito.run(-velocidade_padrão)
    PararMotores()
   
def Girar_Para_Grau(grau):
    Turn_Error = (grau - hub.imu.heading())
    while not (Turn_Error == 0):
        Turn_Error = (grau - hub.imu.heading())
        motor_esquerdo.run((Turn_Error * kPTurn) * 100)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 100)
    PararMotores()

def Meia_Volta():
    print("MEIA VOLTA")
    hub.display.number(18)
    DoisMotores(100)
    Girar180()
    DoisMotoresGiro(400, -400, 1500)
    DoisMotoresGiro(400, 400, 900)
    hub.display.off()


 
#================================================#
# seguir linha com PID
def Seguidor_de_Linha():
    print('Trocando para Seguidor de linha!') 
    global estado, last_error, lastTime
    while True:

        pitch, roll = hub.imu.tilt(True)

        data = hub.ble.observe(2)
        
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
            hub.speaker.beep()
            estado = 5
            return
        if Button.RIGHT in pressed:
            hub.speaker.beep()
            estado = 1
            return

        # Correção de curvas
        if (sensor_1.reflection() < 30) and (sensor_2.reflection() < 40) and not (sensor_3.reflection() < 38):
            DoisMotores(190)
            DoisMotoresGiro(-1000, 1000, 400)
            if sensor_3.reflection() < 20:
                DoisMotoresGiro(1000, -1000, 400)
            while not (sensor_2.reflection() < 30):
                DoisMotoresGiroSemTempo(400, -1000)
            DoisMotoresGiro(1000, -1000, 500)
        
            PararMotores()
 
        elif (sensor_4.reflection() < 30) and (sensor_3.reflection() < 40) and not (sensor_2.reflection() < 38):
            DoisMotores(190)
            DoisMotoresGiro(1000, -1000, 400)
            if sensor_2.reflection() < 20:
                DoisMotoresGiro(-1000, 1000, 400)
            while not (sensor_3.reflection() < 30):
                DoisMotoresGiroSemTempo(-1000, 400)    
            DoisMotoresGiro(-1000, 1000, 500)
            PararMotores()
        '''if data is not None:
            if data == ('resgate'):
                if sensor_1.reflection() < 40 or sensor_2.reflection() < 40 or sensor_3.reflection() < 40 or sensor_4.reflection() < 40:
                    hub.ble.broadcast("AlarmeFalso")
                    continue 
                else:
                    DoisMotoresGiro(1000, -1000, 400)
                    if sensor_1.reflection() < 40 or sensor_2.reflection() < 40 or sensor_3.reflection() < 40 or sensor_4.reflection() < 40:
                        hub.ble.broadcast("AlarmeFalso")
                        DoisMotoresGiro(-1000, 1000, 400)
                        continue 
                    else:
                        DoisMotoresGiro(1000, 1000, 700)
                        if sensor_1.reflection() < 40 or sensor_2.reflection() < 40 or sensor_3.reflection() < 40 or sensor_4.reflection() < 40:
                            hub.ble.broadcast("AlarmeFalso")
                            continue 
                        else:
                            DoisMotoresGiro(-1000, 1000, 400)
                            hub.ble.broadcast("Resgate")
                            wait(2000)
                            hub.ble.broadcast("Nada")
                            wait(1000)
                            estado = 4
                            return'''
                
        if data == 'obstaculo':
            PararMotores()
            estado = 3
            return
       
        # Verificação de cor verde
        if sensor_1.color() == Color.GREEN or sensor_2.color() == Color.GREEN or sensor_3.color() == Color.GREEN or sensor_4.color() == Color.GREEN:
            PararMotores()
            print("Verde!")
            estado = 2
            return
        print (pitch)
        if (sensor_1.reflection() > 85 or sensor_2.reflection() > 85 or sensor_3.reflection() > 85 or sensor_4.reflection() > 85) and (sensor_1.reflection() > 40 and sensor_2.reflection() > 40 and sensor_3.reflection() > 40 and sensor_4.reflection() > 40):
            PararMotores()
            print("Vi prata em gay")
            print("Resgate!")
            estado = 4
            return
            '''
            DoisMotoresGiro(-1000, 1000, 500)
            if (sensor_1.color() != Color.BLACK and sensor_2.color() != Color.BLACK and sensor_3.color() != Color.BLACK or sensor_4.color() != Color.BLACK):
                DoisMotoresGiro(1000, -1000, 500)
                print("Resgate!")
                estado = 4
                return'''
            
           
        if sensor_1.color() == Color.RED or sensor_2.color() == Color.RED or sensor_3.color() == Color.RED or sensor_4.color() == Color.RED:
            PararMotores()
            estado = 6
            return

        # PID básico
        error = (53 - sensor_1.reflection()) + (40 - sensor_2.reflection()) - ((40 - sensor_3.reflection()) + (53 - sensor_4.reflection()))
        # Calcula deltaTime evitando divisão por zero
        deltaTime = max((cronometro.time() / 1000) - lastTime, 0.001)
        Derivative = (error - last_error) / deltaTime
        correcao = ((error * kP) + (Derivative * kD))
        # Se estiver fora da linha
        if (sensor_1.reflection() > 40) and (sensor_2.reflection() > 50) and (sensor_3.reflection() > 50) and (sensor_4.reflection() > 40):
            correcao = 0
        motor_esquerdo.run(650 + correcao)
        motor_direito.run(650 - correcao)
        last_error = error
        lastTime = cronometro.time() / 1000
#================================================#
def Verde():
    #print('Trocando para Verde!')  
    global estado
    while True:
        
        pressed = hub.buttons.pressed()

        if Button.LEFT in pressed:
            estado = 5
            return
        if Button.RIGHT in pressed:
            estado = 1
            return

        hub.imu.reset_heading(0)

        if sensor_2.color() == Color.GREEN and sensor_3.color() == Color.GREEN:
            Meia_Volta()
            estado = 1
            return
        elif sensor_3.color() == Color.GREEN:
            DoisMotores(10)
            if sensor_2.color() == Color.GREEN and sensor_3.color() == Color.GREEN:
                Meia_Volta()
                estado = 1
                return
            DoisMotores(-60)
            if sensor_1.color() == Color.BLACK or sensor_3.color() == Color.BLACK:
                DoisMotores(200)
                estado = 1
                return
            print("Reto")
            DoisMotores(250)
            print("Giro45DireitaAGORA")
            Giro45Direita()
            while sensor_3.color() != Color.BLACK:
                motor_esquerdo.run(-800)
                motor_direito.run(800)
                print('GirandoAtéVerPreto')
            print('Voltando seguidor de linha')
            estado = 1
            return
        elif sensor_2.color() == Color.GREEN:
            DoisMotores(10)
            if sensor_2.color() == Color.GREEN and sensor_3.color() == Color.GREEN:
                Meia_Volta()
            DoisMotores(-60)
            if sensor_2.color() == Color.BLACK or sensor_4.color() == Color.BLACK:
                DoisMotores(200)
                estado = 1
                return
            print("Reto")
            DoisMotores(250)
            print("Giro45EsquerdaAGORA")
            Giro45Esquerda()
            while sensor_2.color() != Color.BLACK:
                motor_esquerdo.run(800)
                motor_direito.run(-800)
                print('GirandoAtéVerPreto')
            print('Voltando seguidor de linha')
            estado = 1
            return
        
        elif sensor_2.color() == Color.GREEN and not (sensor_3.color() == Color.GREEN):
            hub.display.icon(SQUARE_1)
            DoisMotores(10)
            wait(500)
            if sensor_3.color() == Color.GREEN:
                hub.display.number(18)
                Girar180()
                hub.display.off()
            else:
                DoisMotores(350)
                Giro45Esquerda()
                while sensor_3.reflection() < 40:
                    drive_base.turn(700)
                drive_base.turn(-100)
                DoisMotores(100)
                PararMotores()
        elif sensor_3.color() == Color.GREEN and not (sensor_2.color() == Color.GREEN):
            hub.display.icon(SQUARE_2)
            DoisMotores(10)
            wait(500)
            if sensor_3.color() == Color.GREEN:
                hub.display.number(18)
                Girar180()
                hub.display.off()
            else:
                DoisMotores(350)
                Giro45Direita()
                while sensor_3.reflection() < 40:
                    drive_base.turn(-700)
                drive_base.turn(100)
                DoisMotores(100)
                PararMotores()
        estado = 1
        return

#================================================# 
def Obstaculo():
    print('Trocando para Obstáculo!')  
    global estado
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            estado = 5
            return
        if Button.RIGHT in pressed:
            estado = 1
            return

        PararMotores()
        Orientação = hub.imu.heading()
        hub.imu.reset_heading(0)
        DoisMotoresGiro(-1000, -1000, 300)
        Giro90Direita()
        PararMotores()
        DoisMotoresGiro(1000, 1000, 2000)
        Giro90Esquerda()
        DoisMotoresGiro(1000, 1000, 4500)
        Giro90Esquerda()
        while not (sensor_1.color() == Color.BLACK) and not (sensor_2.color() == Color.BLACK):
            DoisMotoresGiroSemTempo(800, 800)
        PararMotores()
        DoisMotoresGiro(1000, 1000, 600)
        Giro90Direita()
        DoisMotoresGiro(-1000, -1000, 500)
        estado = 1
        return
#================================================ 
def AreaDeResgate():
    print('Trocando para Area De Resgate!')  
    global estado
    global resgate
    resgate = 1
    vitimas = 0
    keyboard = poll()
    keyboard.register(stdin)
    wait(3000)
    stdout.buffer.write(b"rdy")
    hub.ble.broadcast("Resgate")
    wait(1000)
    hub.ble.broadcast("nada")
    DoisMotoresGiro(1000, 1000, 2000)
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            estado = 5
            return
        if Button.RIGHT in pressed:
            hub.ble.broadcast("AlarmeFalso")
            estado = 1
            resgate = 0
            return

        while not keyboard.poll(0):
            wait(10)
        cmd = stdin.buffer.read(3)

        data = hub.ble.observe(2)

        if cmd == b"lft":
            motor_esquerdo.run(-70)
            motor_direito.run(70)
        elif cmd == b"rgt":
            motor_esquerdo.run(70)
            motor_direito.run(-70)
        elif cmd == b"rgr":
            motor_esquerdo.run(-500)
            motor_direito.run(500)
        elif cmd == b"stp":
            motor_esquerdo.stop()
            motor_direito.stop()
        elif cmd == b"fwd":
            motor_esquerdo.run(150)
            motor_direito.run(150)
        elif cmd == b"fwr":
            motor_esquerdo.run(480)
            motor_direito.run(480)
        elif cmd == b"frr":
            motor_esquerdo.run(1000)
            motor_direito.run(1000)
        elif cmd == b"stp":
            motor_esquerdo.brake()
            motor_direito.brake()
        elif cmd == b"cnt":
            continue
        elif cmd == b"viv":
            vitimas += 1
            DoisMotoresGiro(-500, -500, 200)
            hub.ble.broadcast("viva")
            wait(1000)
            DoisMotoresGiro(-700, -700, 1000)
            hub.ble.broadcast("para")
            wait(1000)
        elif cmd == b"mrt":
            vitimas += 1
            DoisMotoresGiro(-500, -500, 200)
            hub.ble.broadcast("morta")
            wait(1000)
            DoisMotoresGiro(-700, -700, 1000)
            hub.ble.broadcast("para")
            wait(1000)     
        elif cmd == b"tri":
            Giro180Direita()
            DoisMotoresGiro(-1000, -1000, 3000)
            DoisMotoresGiro(700, 700, 700)
            DoisMotoresGiro(-700, -700, 300)
            wait(500)
            hub.ble.broadcast("Direita")
            wait(1000)
            hub.ble.broadcast("para")
            wait(1000)
            DoisMotoresGiro(500, 500, 800)
            DoisMotoresGiro(-1000, -1000, 600)
            DoisMotoresGiro(1000, 1000, 2000)
            wait(1000)
            break
        elif cmd == b"trv":
            Giro180Direita()
            DoisMotoresGiro(-1000, -1000, 3000)
            DoisMotoresGiro(700, 700, 700)
            DoisMotoresGiro(-700, -700, 300)
            wait(500)
            hub.ble.broadcast('Esquerda')
            wait(1000)
            hub.ble.broadcast("para")
            wait(1000)
            DoisMotoresGiro(500, 500, 800)
            DoisMotoresGiro(-1000, -1000, 600)
            DoisMotoresGiro(1000, 1000, 2000)
            wait(1000)
            continue
        elif cmd == b"bye":
            break
        else:
            motor_esquerdo.stop()
            motor_direito.stop()         
#================================================#

def ProcuraSaida():
    global estado
    data = None
    while not (sensor_1.color() == Color.BLACK or sensor_2.color() == Color.BLACK or sensor_3.color() == Color.BLACK or sensor_4.color() == Color.BLACK or sensor_1.reflection() > 90 or sensor_2.reflection() > 90 or sensor_3.reflection() > 90 or sensor_4.reflection() > 90 or data == "TentaDenovo"):
            data = hub.ble.observe(2)
            DoisMotoresGiroSemTempo(1000, 1000)
    PararMotores()
    if sensor_1.color() == Color.BLACK or sensor_2.color() == Color.BLACK or sensor_3.color() == Color.BLACK or sensor_4.color() == Color.BLACK:
            print("seguir linha pae")
            estado = 1
            hub.ble.broadcast("Saiu")
            wait(1000)
            return
    elif sensor_1.reflection() > 90 or sensor_2.reflection() > 90 or sensor_3.reflection() > 90 or sensor_4.reflection() > 90:
            DoisMotoresGiro(-1000, -1000, 4000)
            Giro90Direita()
            DoisMotoresGiro(-1000, -1000, 4000)
            return
    elif data == "TentaDenovo":
            DoisMotoresGiro(-1000, -1000, 4000)
            Giro90Direita()
            DoisMotoresGiro(-1000, -1000, 4000)
            return
    else:
        print('Sei la man')
            

#================================================#
def Verificacao():
    global estado
    while True:
        if estado == 1:
            return
        hub.ble.broadcast("CadeSaida")
        wait(1000)
        data = hub.ble.observe(2)
        if data == "SaidaEsquerda":
            print("Tem Coisa")
            Giro90Esquerda()
            ProcuraSaida()
            return
        if data == "SaidaDireita":
            print("Tem Coisa")
            Giro90Direita()
            ProcuraSaida()
            return
        if data == "NaoTem":
            print("Tem Nada")
            return
#================================================#
def Saida():
    global estado
    Giro45Direita()
    hub.ble.broadcast("CadeSaida")
    wait(1000)
    data = hub.ble.observe(2)
    if data == "SaidaFrente":
        ProcuraSaida()
    elif data == "SaidaEsquerda":
        Giro90Esquerda()
        ProcuraSaida()
    elif data == "SaidaDireita":
        Giro90Direita()
        ProcuraSaida()
    elif data == "NaoTem":
        Giro90Direita()

    hub.ble.broadcast("CadeSaida")
    wait(1000)
    data = hub.ble.observe(2)
    if data == "SaidaDireita":
        Giro90Direita()
        ProcuraSaida()
    while True:
        if estado == 1:
            return
        DoisMotoresGiro(-1000, -1000, 5000)
        Verificacao()
        if estado == 1:
            return
        DoisMotoresGiro(1000, 1000, 2100)
        Verificacao()
        if estado == 1:
            return
        DoisMotoresGiro(1000, 1000, 2900)
        Verificacao()
        if estado == 1:
            return
        DoisMotoresGiro(1000, 1000, 2500)
        Verificacao()
        if estado == 1:
            return
        DoisMotoresGiro(-1000, -1000, 3500)
        Giro90Direita()

def parar():
    global estado
    while True:
        pressed = hub.buttons.pressed()
        if Button.LEFT in pressed:
            hub.speaker.beep()
            estado = 1
            return
        if Button.RIGHT in pressed:
            hub.speaker.beep()
            estado = 1
            return
        PararMotores()
#================================================#
'''
hub.speaker.volume(70)
hub.speaker.play_notes([
    "E4/8", "E4/8", "E4/8",
    "C4/8", "E4/8", "G4/4",
    "G3/4", "C4/4",
    "G3/4", "E3/4",
    "A3/4", "B3/4", "Bb3/8", "A3/8",
    "G3/4", "E4/8", "G4/8", "A4/8",
    "F4/8", "G4/8", "E4/8", "C4/8",
    "D4/8", "B3/8"
])
'''

#================================================#
while True:
    if estado == 1:
        Seguidor_de_Linha()
    elif estado == 2:
        Verde()
    elif estado == 3:
        Obstaculo()
    elif estado == 4:
        AreaDeResgate()
    elif estado == 5:
        parar()
    elif estado == 6:
        print("Cabô")
        PararMotores()
        hub.system.shutdown()
    elif estado == 7:
        Saida()
        
#================================================#