# Control Háptico para Drones con MPU6050

Proyecto que permite controlar un dron mediante movimientos de la mano, utilizando un sensor **MPU6050** que es un acelerómetro y giroscopio integrado en una PCB personalizada junto a una ESP-32 y un script en Python que recibe los datos por comunicacion serial del ESP-32 para enviar instrucciones de vuelo.

## Características principales
- **Control por movimientos**: Inclina tu mano para dirigir el dron.
- **PCB personalizada**: Diseño optimizado para el sensor MPU6050.
- **Software en Python**: Procesamiento de datos y comunicación con el dron.
- **Bajo costo**: Hardware accesible y código abierto.

## Hardware
### Componentes
- Sensor MPU6050 PCB personalizada
- Microcontrolador ESP32
- controlador de Dron con comunicacion Wifi
- Fuente de alimentación Batería LiPo 3.7V

### Diagrama de conexión
```plaintext
MPU6050 (PCB) → Microcontrolador → Python (PC) → WIFI → Dron
