from DroneController import Drone
import serial
import time

class DroneControllerSerial:
    def __init__(self, serial_port='COM13', baudrate=115200):
        self.drone = Drone()
        self.serial_conn = serial.Serial(serial_port, baudrate, timeout=1)
        self.current_command = None
        self.last_command_time = 0
        self.command_timeout = 0.5  # segundos sin comando antes de hover

    def start(self):
        print("Conectando con el dron...")
        self.drone.connect()
        self.drone.calibrate()
        self.drone.take_off(wait=1)
        
        print("Iniciando control por MPU6050...")
        try:
            while True:
                self.read_serial()
                self.execute_command()
        except KeyboardInterrupt:
            print("Finalizando...")
            self.drone.land(wait=3)
            self.drone.disconnect()
            self.serial_conn.close()

    def read_serial(self):
        if self.serial_conn.in_waiting > 0:
            line = self.serial_conn.readline().decode('utf-8').strip()
            if line.startswith("Dirección:"):
                self.current_command = line.split(":")[1].strip().lower()
                self.last_command_time = time.time()
                print(f"Comando recibido: {self.current_command}")

    def execute_command(self):
        now = time.time()
        if now - self.last_command_time > self.command_timeout:
            self.current_command = None
        
        if self.current_command is None:
            self.drone.hover(wait=0.1)
        else:
            if self.current_command == "adelante":
                self.drone.move('forward', speed=30, wait=0.1)
            elif self.current_command == "atrás":
                self.drone.move('backward', speed=30, wait=0.1)
            elif self.current_command == "izquierda":
                self.drone.rotate('left', speed=30, wait=0.1)
            elif self.current_command == "derecha":
                self.drone.rotate('right', speed=30, wait=0.1)
            else:
                self.drone.hover(wait=0.1)

if __name__ == "__main__":
    controller = DroneControllerSerial()
    controller.start()