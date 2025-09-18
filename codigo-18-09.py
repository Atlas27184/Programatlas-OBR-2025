from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port
from pybricks.tools import wait, StopWatch, Matrix
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
hub = PrimeHub()

sensor_1 = ColorSensor(Port.A)
sensor_2 = ColorSensor(Port.B)
sensor_3 = ColorSensor(Port.C)
sensor_4 = ColorSensor(Port.D)
sensor_1.detectable_colors([Color.GREEN, Color.BLACK, Color.WHITE, Color.RED])
sensor_2.detectable_colors([Color.GREEN, Color.BLACK, Color.WHITE, Color.RED])
sensor_3.detectable_colors([Color.GREEN, Color.BLACK, Color.WHITE, Color.RED])
sensor_4.detectable_colors([Color.GREEN, Color.BLACK, Color.WHITE, Color.RED])

motor_esquerdo = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.F)

hub.imu.reset_heading(0)
cronometro = StopWatch()
cronometro.reset()

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

velocidade_padrão = 740
kP = 1 * 18.5
kD = 0
kPTurn = 1

#================================================#
# Funções auxiliares
def PararMotores():
    motor_esquerdo.hold()
    motor_direito.hold()

def DoisMotoresAngulo(velocidade, angulo):
    motor_esquerdo.run_angle(velocidade, angulo)
    motor_direito.run_angle(velocidade, angulo)

def DoisMotores(velocidade):
    motor_esquerdo.run(velocidade)
    motor_direito.run(velocidade)

def Giro90Esquerda():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação - 90) - hub.imu.heading()
    while not (Turn_Error == 0):
        Turn_Error = (Orientação - 90) - hub.imu.heading()
        motor_esquerdo.run((Turn_Error * kPTurn) * 10)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 10)
    PararMotores()

def Giro90Direita():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 90) - hub.imu.heading()
    while not (Turn_Error == 0):
        Turn_Error = (Orientação + 90) - hub.imu.heading()
        motor_esquerdo.run((Turn_Error * kPTurn) * 10)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 10)
    PararMotores()

def Giro45Esquerda():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação - 45) - hub.imu.heading()
    while not (Turn_Error == 0):
        Turn_Error = (Orientação - 45) - hub.imu.heading()
        motor_esquerdo.run((Turn_Error * kPTurn) * 10)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 10)
    PararMotores()

def Giro45Direita():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 45) - hub.imu.heading()
    while not (Turn_Error == 0):
        Turn_Error = (Orientação + 45) - hub.imu.heading()
        motor_esquerdo.run((Turn_Error * kPTurn) * 10)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 10)
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
# Classe de seguir linha com PID
class SeguirLinha:
    def __init__(self, fsm):
        self.fsm = fsm
        self.lastTime = cronometro.time() / 1000
        self.last_error = 0.0

    def run(self):
        while True:
            # Verificação de cor verde
            
                # TODO: enviar para estado verde
                

            # Correção de curvas (exemplo simplificado)
            if (sensor_1.reflection() < 20) and (sensor_2.reflection() < 20) and not (sensor_3.reflection() < 20):
                DoisMotoresAngulo(velocidade_padrão, 400)
                wait(1000)
                motor_esquerdo.run_angle(-velocidade_padrão, 50)
                motor_direito.run_angle(velocidade_padrão, 50)
                if sensor_1.reflection() < 20:
                    motor_esquerdo.run_angle(velocidade_padrão, 50)
                    motor_direito.run_angle(-velocidade_padrão, 50)
    
                while sensor_3.reflection() < 40:
                    motor_esquerdo.run(-_40_porcento)
                    motor_direito.run(_70_porcento)
    
                    PararMotores()

            elif (sensor_4.reflection() < 20) and (sensor_3.reflection() < 20) and not (sensor_2.reflection() < 20):
                DoisMotoresAngulo(velocidade_padrão, 400)
                wait(1000)
    
                motor_esquerdo.run_angle(velocidade_padrão, 50)
                motor_direito.run_angle(-velocidade_padrão, 50)
    
                if sensor_4.reflection() < 20:
                    motor_esquerdo.run_angle(-velocidade_padrão, 50)
                    motor_direito.run_angle(velocidade_padrão, 50)
    
                while sensor_2.reflection() < 40:
                    motor_esquerdo.run(-_40_porcento)
                    motor_direito.run(_70_porcento)
    
                    PararMotores()
            # Aqui você pode colocar as condições específicas de cada curva que você tinha

            # PID básico
            error = ((100 - sensor_1.reflection()) + (100 - sensor_2.reflection())) - ((100 - sensor_3.reflection()) + (100 - sensor_4.reflection()))

            # Calcula deltaTime evitando divisão por zero
            deltaTime = max((cronometro.time() / 1000) - self.lastTime, 0.001)

            Derivative = (error - self.last_error) / deltaTime

            correcao = ((error * kP) + (Derivative * kD))

            # Se estiver fora da linha
            if (sensor_1.reflection() > 80) and (sensor_2.reflection() > 80) and (sensor_3.reflection() > 80) and (sensor_4.reflection() > 80):
                correcao = 0
        
            print(correcao)
            motor_esquerdo.run(400 - correcao) 
            motor_direito.run(400 + correcao)

            self.last_error = error
            self.lastTime = cronometro.time() / 1000
#================================================#
# Classe Verde
class Verde():
    def __init__(self, fsm):
        self.fsm = fsm

    def run(self):
        hub.imu.heading(0)
        if sensor_1.color() == Color.GREEN:
            while sensor_1.color() == Color.GREEN:
                motor_esquerdo.run(-_30_porcento)
                motor_direito.run(_30_porcento)
            PararMotores()
        elif sensor_1.color() == Color.GREEN:
                while sensor_1.color() == Color.GREEN:
                    motor_esquerdo.run(_30_porcento)
                    motor_direito.run(-_30_porcento)
                PararMotores()
        elif sensor_3.color() == Color.GREEN:
            DoisMotoresAngulo(-velocidade_padrão, 80)
            if sensor_1.color() == Color.BLACK and sensor_3.color() == Color.BLACK:
                DoisMotoresAngulo(velocidade_padrão, 300)
                # MANDAR SEGUIDOR DE LINHA!!!!
            DoisMotoresAngulo(velocidade_padrão, 100)
        elif sensor_2.color() == Color.GREEN:
            DoisMotoresAngulo(-velocidade_padrão, 80)
            if sensor_2.color() == Color.BLACK and sensor_4.color() == Color.BLACK:
                DoisMotoresAngulo(velocidade_padrão, 300)
                # MANDAR SEGUIDOR DE LINHA!!!!
            DoisMotoresAngulo(velocidade_padrão, 100)
        elif sensor_2.color() == Color.GREEN and sensor_3.color() == Color.GREEN:
            hub.display.number(18)
            Girar180()
            hub.display.off
        elif sensor_2.color() == Color.GREEN and not (sensor_3.color() == Color.GREEN):
            hub.display.icon(SQUARE_1)
            DoisMotoresAngulo(velocidade_padrão, 15)
            wait(500)
            if sensor_3.color() == Color.GREEN:
                hub.display.number(18)
                Girar180()
                hub.display.off
            else: 
                DoisMotoresAngulo(velocidade_padrão, 350)
                Giro45Esquerda()
                while sensor_3.reflection() < 40:
                    motor_esquerdo.run(-70)
                    motor_direito.run(40)
                motor_esquerdo.run_angle(velocidade_padrão, 100)
                motor_direito.run_angle(-velocidade_padrão, 100)
                DoisMotoresAngulo(velocidade_padrão, 100)
                PararMotores()
        elif sensor_3.color() == Color.GREEN and not (sensor_2.color() == Color.GREEN):
            hub.display.icon(SQUARE_2)
            DoisMotoresAngulo(velocidade_padrão, 15)
            wait(500)
            if sensor_3.color() == Color.GREEN:
                hub.display.number(18)
                Girar180()
                hub.display.off
            else: 
                DoisMotoresAngulo(velocidade_padrão, 350)
                Giro45Direita()
                while sensor_3.reflection() < 40:
                    motor_esquerdo.run(40)
                    motor_direito.run(-70)
                motor_esquerdo.run_angle(-velocidade_padrão, 100)
                motor_direito.run_angle(velocidade_padrão, 100)
                DoisMotoresAngulo(velocidade_padrão, 100)
                PararMotores()
        #ENVIAR SEGUIDOR DE LINHAAA!!!!!!!!!

#================================================#
#QUANDO RECEBER OBSTÁCULO
Orientação = hub.imu.heading()
hub.imu.heading(0)
DoisMotoresAngulo(velocidade_padrão, 150)
Giro90Direita()
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
#SEGUIDOR DE LINHAAAAA
#================================================#
fsm = None
seguir = SeguirLinha(fsm)
seguir.run()
#================================================#
'''hub.speaker.volume(100)
hub.speaker.play_notes([
 "E4/8", "E4/8", "E4/8", 
    "C4/8", "E4/8", "G4/4", 
    "G3/4", "C4/4", 
    "G3/4", "E3/4", 
    "A3/4", "B3/4", "Bb3/8", "A3/8", 
    "G3/4", "E4/8", "G4/8", "A4/8", 
    "F4/8", "G4/8", "E4/8", "C4/8", 
    "D4/8", "B3/8"
])'''
#================================================#
