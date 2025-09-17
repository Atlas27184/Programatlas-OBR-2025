from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# sensor de cor 1 - Porta A 
# sensor de cor 2 - Porta B
# sensor de cor 3 - Porta C 
# sensor de cor 4 - Porta D
# motor esquerdo - Porta E
# motor direito - Porta F

#================================================#
sensor_1 = ColorSensor(Port.A)
sensor_2 = ColorSensor(Port.B)
sensor_3 = ColorSensor(Port.C)
sensor_4 = ColorSensor(Port.D)
motor_esquerdo = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motor_direito = Motor(Port.F)

kP = 1.5
kD = 0.1
kPTurn = 1 
last_error = 0
area_de_resgate = 0
ocupado = 0
hub.imu.reset_heading(0)
#================================================#
def Giro90Esquerda():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação - 90) - hub.imu.heading()
    while not (Turn_Error == 0):
        Turn_Error = (Orientação - 90) - hub.imu.heading()
        motor_esquerdo.run((Turn_Error * kPTurn) * 10)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 10)
    motor_esquerdo.brake()
    motor_direito.brake()

def Giro90Direita():
    Orientação = hub.imu.heading()
    Turn_Error = (Orientação + 90) - hub.imu.heading()
    while not (Turn_Error == 0):
        Turn_Error = (Orientação + 90) - hub.imu.heading()
        motor_esquerdo.run((Turn_Error * kPTurn) * 100)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 100)
    motor_esquerdo.brake()
    motor_direito.brake()

def Girar_Para_Grau(grau):
    Turn_Error = (grau - hub.imu.heading())
    while not (Turn_Error == 0):
        Turn_Error = (grau - hub.imu.heading())
        motor_esquerdo.run((Turn_Error * kPTurn) * 100)
        motor_direito.run(((Turn_Error * -1) * kPTurn) * 100)
    motor_esquerdo.brake()
    motor_direito.brake()
#================================================#
class SeguirLinha:
    def _init_(self, fsm):
        self.fsm = fsm
    
    def run(self):
        while True:
            if sensor_1.color() = Color.GREEN or sensor_2.color() = Color.GREEN or sensor_3.color() = Color.GREEN or sensor_4.color() = Color.GREEN:
                motor_esquerdo.brake()
                motor_direito.brake()
                #ARRUMAR UM JEITO DE ENVIAR PRO ESTADO VERDE
                break
            elif (sensor_1.reflection() < 20%) and (sensor_2.reflection() < 20%) and not (sensor_3.reflection() < 20%):
                motor_esquerdo.run_angle(1000, 400)
                motor_direito.run_angle(1000, 400)
                wait(100)
                motor_esquerdo.run_angle(1000, 50)
                motor_direito.run_angle(-1000, 50)
                
#================================================#
