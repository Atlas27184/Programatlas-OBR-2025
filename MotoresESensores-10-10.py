from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port
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
kPTurn = 1
lastTime = cronometro.time() / 1000
last_error = 0.0    
estado = 1
#================================================#
# Funções auxiliares
def PararMotores():
    motor_esquerdo.hold()
    motor_direito.hold()
 
def DoisMotores(velocidade):
    drive_base.straight(velocidade)

def DoisMotoresGiroSemTempo(velocidade_esquerda, velocidade_direita):
    motor_esquerdo.run(velocidade_esquerda)
    motor_direito.run(velocidade_direita)
 
def DoisMotoresGiro(velocidade_esquerda, velocidade_direita, tempo):
    motor_esquerdo.run(velocidade_esquerda)
    motor_direito.run(velocidade_direita)
    wait(tempo)
    PararMotores()
 
def Giro90Esquerda():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 90) - hub.imu.heading()
    while not (Turn_Error < 1) or not (Turn_Error > -1):
        Turn_Error = (Orientação + 90) - hub.imu.heading()
        motor_esquerdo.run((Turn_Error * kPTurn) * 10)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 10)
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
        if (Turn_Error < 1) and (Turn_Error > -1):
            break
    PararMotores()
 
def Giro45Direita():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 45) - hub.imu.heading()
    while not (Turn_Error < 1) or not (Turn_Error > -1):
        Turn_Error = (Orientação + 45) - hub.imu.heading()
        print(Turn_Error)
        motor_esquerdo.run(((Turn_Error * -1) * kPTurn) * 10)
        motor_direito.run((Turn_Error * kPTurn) * 10)
        if (Turn_Error < 1) and (Turn_Error > -1):
            break
    PararMotores()
 
def Girar180():
    motor_esquerdo.run_angle(velocidade_padrão, 1400)
    motor_direito.run_angle(-velocidade_padrão, 1400)
    while sensor_2.color() != Color.BLACK:
        motor_esquerdo.run(velocidade_padrão)
        motor_direito.run(-velocidade_padrão)
    DoisMotoresAngulo(velocidade_padrão, 100)
    PararMotores()
   
def Girar_Para_Grau(grau):
    Turn_Error = (grau - hub.imu.heading())
    while not (Turn_Error == 0):
        Turn_Error = (grau - hub.imu.heading())
        motor_esquerdo.run((Turn_Error * kPTurn) * 100)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 100)
    PararMotores()
 
#================================================#
# seguir linha com PID
def Seguidor_de_Linha():
    #print('Trocando para Seguidor de linha!') 
    h1, s1, v1 = sensor_1.hsv()
    h2, s2, v2 = sensor_2.hsv()
    h3, s3, v3 = sensor_3.hsv()
    h4, s4, v4 = sensor_4.hsv()
    global estado, last_error, lastTime
    while True:
        # print(sensor.color)  # Mostra (hue, saturation, value)
        '''
        print('Próximo')
        print(sensor_1.reflection(), sensor_2.reflection(), sensor_3.reflection(), sensor_4.reflection())
        '''
        '''
        print("HSV:", h1, s1, v1, " | Cor:", sensor_1.color())
        print("HSV:", h2, s2, v2, " | Cor:", sensor_2.color())
        print("HSV:", h3, s3, v3, " | Cor:", sensor_3.color())
        print("HSV:", h4, s4, v4, " | Cor:", sensor_4.color())
        wait(500) '''
        # Recebe obstáculo
        data = hub.ble.observe(2)
           
        # Correção de curvas
        if (sensor_1.reflection() < 30) and (sensor_2.reflection() < 40) and not (sensor_3.reflection() < 38):
            DoisMotores(100)
            DoisMotoresGiro(-1000, 1000, 700)
            #if sensor_1.reflection() < 20:
                #DoisMotoresGiro(-1000, 1000, 600)
            while not (sensor_2.reflection() < 30):
                DoisMotoresGiroSemTempo(_50_porcento, -_50_porcento)
            DoisMotoresGiro(700, -700, 1300)
            PararMotores()
 
        elif (sensor_4.reflection() < 30) and (sensor_3.reflection() < 40) and not (sensor_2.reflection() < 38):
            DoisMotores(100)
            DoisMotoresGiro(1000, -1000, 700)
            #if sensor_4.reflection() < 20:
                #DoisMotoresGiro(1000, -1000, 600)
            while not (sensor_3.reflection() < 30):
                DoisMotoresGiroSemTempo(-_50_porcento, _50_porcento)
            DoisMotoresGiro(-700, 700, 1300)
            PararMotores()
        if data is not None:
            if data == ('resgate'):
                if (sensor_1.color() != Color.BLACK) and (sensor_2.color() != Color.BLACK) and (sensor_3.color() != Color.BLACK) and (sensor_4.color() != Color.BLACK):
                    estado = 4
                    return
                else:
                    hub.ble.broadcast('AlarmeFalso')
                    continue
            elif data == 'obstaculo':
                PararMotores()
                estado = 3
                return
       
        # Verificação de cor verde
        
        if sensor_1.color() == Color.GREEN or sensor_2.color() == Color.GREEN or sensor_3.color() == Color.GREEN or sensor_4.color() == Color.GREEN:
            PararMotores()
            estado = 2
            return
           
        if sensor_1.color() == Color.RED or sensor_2.color() == Color.RED or sensor_3.color() == Color.RED or sensor_4.color() == Color.RED:
            PararMotores()
            estado = 5
            return
        
        if sensor_1.reflection() < 30 and sensor_2.reflection() >= 38 and sensor_3.reflection() >= 38 and sensor_4.reflection() >= 38:
            while not sensor_2.reflection() < 30:
                DoisMotoresGiroSemTempo(500, -500)
            PararMotores()
        
        elif sensor_4.reflection() < 30 and sensor_3.reflection() >= 38 and sensor_2.reflection() >= 38 and sensor_1.reflection() >= 38:
            while not sensor_3.reflection() < 30:
                DoisMotoresGiroSemTempo(-500, 500)
            PararMotores()

        elif sensor_4.reflection() < 30 and sensor_3.reflection() < 30 and sensor_2.reflection() < 30 and sensor_1.reflection() >= 38:
            while not sensor_2.reflection() >= 38:
                DoisMotoresGiroSemTempo(-500, 500)
            PararMotores()
        
        elif sensor_1.reflection() < 30 and sensor_2.reflection() < 30 and sensor_3.reflection() < 30 and sensor_4.reflection() >= 38:
            while not sensor_3.reflection() >= 38:
                DoisMotoresGiroSemTempo(-500, 500)
            PararMotores()

        # PID básico
        error = (53 - sensor_1.reflection()) + (40 - sensor_2.reflection()) - ((40 - sensor_3.reflection()) + (53 - sensor_4.reflection()))
        # Calcula deltaTime evitando divisão por zero
        deltaTime = max((cronometro.time() / 1000) - lastTime, 0.001)
        Derivative = (error - last_error) / deltaTime
        correcao = ((error * kP) + (Derivative * kD))
        # Se estiver fora da linha
        if (sensor_1.reflection() > 40) and (sensor_2.reflection() > 50) and (sensor_3.reflection() > 50) and (sensor_4.reflection() > 40):
            correcao = 0
        motor_esquerdo.run(350 + correcao)
        motor_direito.run(350 - correcao)
        last_error = error
        lastTime = cronometro.time() / 1000
#================================================#
def Verde():
    #print('Trocando para Verde!')  
    global estado
    h1, s1, v1 = sensor_1.hsv()
    h2, s2, v2 = sensor_2.hsv()
    h3, s3, v3 = sensor_3.hsv()
    h4, s4, v4 = sensor_4.hsv()
    while True:
        # print(sensor.color)  # Mostra (hue, saturation, value) 
        '''
        print('Próximo')
        print("HSV:", h1, s1, v1, " | Cor:", sensor_1.color())
        print("HSV:", h2, s2, v2, " | Cor:", sensor_2.color())
        print("HSV:", h3, s3, v3, " | Cor:", sensor_3.color())
        print("HSV:", h4, s4, v4, " | Cor:", sensor_4.color())
        wait(500) '''
        hub.imu.reset_heading(0)
        if sensor_3.color() == Color.GREEN:
            DoisMotores(-100)
            if sensor_1.color() == Color.BLACK or sensor_3.color() == Color.BLACK:
                DoisMotores(300)
                estado = 1
                return
            print("Reto")
            DoisMotores(400)
            print("Giro45DireitaAGORA")
            Giro45Direita()
            while sensor_3.color() != Color.BLACK:
                motor_esquerdo.run(-300)
                motor_direito.run(300)
                print('GirandoAtéVerPreto')
            print('Voltando seguidor de linha')
            estado = 1
            return
        elif sensor_2.color() == Color.GREEN:
            DoisMotores(-100)
            if sensor_2.color() == Color.BLACK or sensor_4.color() == Color.BLACK:
                DoisMotores(300)
                estado = 1
                return
            DoisMotores(100)
        elif sensor_2.color() == Color.GREEN and sensor_3.color() == Color.GREEN:
            hub.display.number(18)
            Girar180()
            hub.display.off()
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
    '''
    PararMotores()
    Orientação = hub.imu.heading()
    hub.imu.reset_heading(0)
    DoisMotores(-150)
    Giro90Direita()
    PararMotores()
    DoisMotoresAngulo(velocidade_padrão, 800)
    Giro90Esquerda()
    DoisMotoresAngulo(velocidade_padrão, 1800)
    Giro90Esquerda()
    while not (sensor_1.color() == Color.BLACK) and not (sensor_2.color() == Color.BLACK):
        DoisMotores(velocidade_padrão)
    PararMotores()
    DoisMotoresAngulo(velocidade_padrão, 200)
    Giro90Direita()
    DoisMotoresAngulo(-velocidade_padrão, 250)
    estado = 1
    '''
    return
#================================================ 
def AreaDeResgate():
    print('Trocando para Area De Resgate!')  
    global estado
    vitimas = 0
    keyboard = poll()
    keyboard.register(stdin)
    wait(3000)
    stdout.buffer.write(b"rdy")
    while True:
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
            motor_esquerdo.run(500)
            motor_direito.run(-500)
        elif cmd == b"stp":
            motor_esquerdo.stop()
            motor_direito.stop()
        elif cmd == b"fwd":
            motor_esquerdo.run(300)
            motor_direito.run(300)
        elif cmd == b"viv":
            vitimas += 1
            hub.ble.broadcast("viva")
            wait(1000)
            hub.ble.broadcast("para")
            wait(7000)
        elif cmd == b"stp":
            motor_esquerdo.brake()
            motor_direito.brake()
        elif cmd == b"cnt":
            continue
        elif cmd == b"mrt":
            vitimas += 1
            hub.ble.broadcast("morta")
            wait(1000)
            hub.ble.broadcast("para")
            wait(7000)     
        elif cmd == b"tri":
            Giro180Direita()
            DoisMotoresGiro(-800, -800, 4500)
            hub.ble.broadcast("AbreMorta")
            wait(4000)
            DoisMotoresGiro(1000, 1000, 2000)
            hub.ble.broadcast("FechaMorta")
            wait(1000)
            continue
        elif cmd == b"trv":
            Giro180Direita()
            DoisMotoresGiro(-800, -800, 4500)
            hub.ble.broadcast('AbreViva')
            wait(4000)
            DoisMotoresGiro(1000, 1000, 2000)
            hub.ble.broadcast('FechaViva')
            wait(1000)
            continue
        elif cmd == b"bye":
            break
        else:
            motor_esquerdo.stop()
            motor_direito.stop()

#================================================ 
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
        print("Cabô")
        PararMotores
        break    

'''
while True:
    h1, s1, v1 = sensor_1.hsv()
    h2, s2, v2 = sensor_2.hsv()
    h3, s3, v3 = sensor_3.hsv()
    h4, s4, v4 = sensor_4.hsv()
    # print(sensor.color)  # Mostra (hue, saturation, value)
    print('Próximo')
    print("HSV:", h1, s1, v1, " | Cor:", sensor_1.color())
    print("HSV:", h2, s2, v2, " | Cor:", sensor_2.color())
    print("HSV:", h3, s3, v3, " | Cor:", sensor_3.color())
    print("HSV:", h4, s4, v4, " | Cor:", sensor_4.color())
    wait(500)
'''
'''
while True:
    error = (60 - sensor_1.reflection()) + (30 - sensor_2.reflection()) - ((30 - sensor_3.reflection()) + (60 - sensor_4.reflection()))
    p_correction = error * 0.1
    drive_base.drive(1000, p_correction)'''

#================================================#
