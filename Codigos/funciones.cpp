#include "funciones.h"

// Variables globales
bool calibracionSolicitada = false;
bool dmpListo = false;
float compensacionYPR[3] = {0, 0, 0};

// Objetos
MPU6050 mpu;
unsigned long ultimoTiempoDebounce = 0;
uint8_t estadoDispositivo;
uint8_t bufferFIFO[64];
Quaternion q;
VectorFloat gravedad;
float ypr[3]; // yaw, pitch, roll

void iniciar_comunicacion_serial() {
  Serial.begin(BAUDRATE);
}

void configurar_pines() {
  pinMode(PIN_BOTON, INPUT_PULLUP);
}

void configurar_mpu6050() {
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
      Wire.begin(PIN_SDA, PIN_SCL);
      Wire.setClock(FRECUENCIA_I2C);
  #endif

  mpu.initialize();
  estadoDispositivo = mpu.dmpInitialize();

  if (estadoDispositivo == 0) {
      mpu.CalibrateAccel(6);
      mpu.CalibrateGyro(6);
      mpu.setDMPEnabled(true);
      dmpListo = true;
  }
}

void verificarBoton() {
  int estadoBoton = digitalRead(PIN_BOTON);
  if (estadoBoton == HIGH && millis() - ultimoTiempoDebounce > RETRASO_DEBOUNCE) {
    calibracionSolicitada = true;
    ultimoTiempoDebounce = millis();
  }
}

void calibrarMPU() {
  if (mpu.dmpGetCurrentFIFOPacket(bufferFIFO)) {
    mpu.dmpGetQuaternion(&q, bufferFIFO);
    mpu.dmpGetGravity(&gravedad, &q);
    mpu.dmpGetYawPitchRoll(ypr, &q, &gravedad);
    
    compensacionYPR[0] = -ypr[0];
    compensacionYPR[1] = -ypr[1];
    compensacionYPR[2] = -ypr[2];
    
    Serial.println("Calibración completada, posición actual = [0,0,0]");
  }
}

void leerYMostrarDatosMPU() {
  if (mpu.dmpGetCurrentFIFOPacket(bufferFIFO)) {
    mpu.dmpGetQuaternion(&q, bufferFIFO);
    mpu.dmpGetGravity(&gravedad, &q);
    mpu.dmpGetYawPitchRoll(ypr, &q, &gravedad);

    float yawCalibrado = ypr[0] + compensacionYPR[0];
    float pitchCalibrado = ypr[1] + compensacionYPR[1];
    float rollCalibrado = ypr[2] + compensacionYPR[2];

    int ejeX = constrain(rollCalibrado * 180/M_PI, -90, 90);
    int ejeY = constrain(pitchCalibrado * 180/M_PI, -90, 90);
    int ejeZ = constrain(yawCalibrado * 180/M_PI, -90, 90);

    if (abs(ejeY) > UMBRAL_MOVIMIENTO || abs(ejeX) > UMBRAL_MOVIMIENTO) {
    if (abs(ejeY) > abs(ejeX)) {
      // Movimiento predominante en pitch (eje Y)
      if (ejeY > 0) {
        Serial.println("Adelante");
        // Aquí puedes añadir acciones para movimiento adelante
      } else {
        Serial.println("Atras");
        // Aquí puedes añadir acciones para movimiento atrás
      }
    } else {
      // Movimiento predominante en roll (eje X)
      if (ejeX < 0) {
        Serial.println("Derecha");
        // Aquí puedes añadir acciones para movimiento derecha
      } else {
        Serial.println("Izquierda");
        // Aquí puedes añadir acciones para movimiento izquierda
      }
    }
  }
  }
  delay(DELAY);
}