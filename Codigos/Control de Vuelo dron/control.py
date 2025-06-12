import serial
from datetime import datetime
from DroneController import Drone

drone = Drone()
ser = serial.Serial(
    port='COM13',      # puerto de comunicacion serial
    baudrate=115200,    # Ajusta al baud rate
    timeout=1         # Timeout en segundos
)

def ejecutar_accion(comando):
    comando = comando.lower().strip()  # Normaliza el texto
    
    if comando == "adelante":
        print("Moviendo hacia ADELANTE")
        drone.move('forward', speed=50, wait=1) 
    elif comando == "atras":
        print("Moviendo hacia ATRÁS")
        drone.move('backward', speed=50, wait=1) 
    elif comando == "izquierda":
        print("Girando a la IZQUIERDA")
        drone.rotate('left', speed=50,wait=1)
    elif comando == "derecha":
        print("Girando a la DERECHA")
        drone.rotate('right', speed=50,wait=1)
    else:
        print(f"Comando no reconocido: '{comando}'")
        drone.hover(wait=1)



try:
        print("Esperando comandos desde el serial...")
        while True:
            if ser.in_waiting:
                linea = ser.readline().decode('utf-8').strip().lower()
                timestamp = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
                ejecutar_accion(linea)

except KeyboardInterrupt:
    print("\nSistema cerrado correctamente")
except Exception as e:
    print(f"\nError: {str(e)}")