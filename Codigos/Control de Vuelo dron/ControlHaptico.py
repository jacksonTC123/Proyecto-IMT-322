import serial
from DroneController import Drone


drone = Drone()
drone.connect()
drone.calibrate()
drone.take_off(wait=0.5)
drone.move("up",speed=50,wait=1)


# Configuración del puerto serial (ajusta a tu dispositivo)
ser = serial.Serial(
    port='COM13',      # Cambia a tu puerto (ej: 'COM3', '/dev/ttyUSB0')
    baudrate=115200,    # Ajusta al baud rate de tu ESP
    timeout=1         # Timeout en segundos
)

def ejecutar_accion(comando):
    """Ejecuta una acción basada en el comando recibido."""
    comando = comando.lower().strip()  # Normaliza el texto
    
    if comando == "adelante":
        print(">>> Moviendo hacia ADELANTE")
        
        drone.move('forward', speed=50, wait=0.5) 
    elif comando == "atras":
        print(">>> Moviendo hacia ATRÁS")
        drone.move('backward', speed=50, wait=0.5) 
    elif comando == "izquierda":
        print(">>> Girando a la IZQUIERDA")
        drone.rotate('left', speed=50,wait=0.5)
    elif comando == "derecha":
        print(">>> Girando a la DERECHA")
        drone.rotate('right', speed=50,wait=1)
    
    else:
        print(f"Comando no reconocido: '{comando}'")
        drone.hover(wait=0.5)

# Bucle principal
try:
    print("Esperando comandos desde el serial...")
    while True:
        if ser.in_waiting > 0:
            ser.reset_input_buffer()
            linea = ser.readline().decode('utf-8').strip()  # Lee y decodifica
            ejecutar_accion(linea)
            drone.hover(wait=0.5)

except KeyboardInterrupt:
    print("\nPrograma terminado.")
    drone.land(wait=1)
    drone.disconnect()  
    ser.close()