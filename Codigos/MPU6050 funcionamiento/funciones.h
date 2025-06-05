#ifndef FUNCIONES_H
#define FUNCIONES_H

#include <Arduino.h>
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"

// Constantes
#define PIN_BOTON          4
#define RETRASO_DEBOUNCE   50
#define BAUDRATE           115200
#define PIN_SDA            21
#define PIN_SCL            22
#define FRECUENCIA_I2C     400000
#define DELAY              50

// Variables globales
extern bool calibracionSolicitada;
extern bool dmpListo;
extern float compensacionYPR[3];

// Configuración inicial
void iniciar_comunicacion_serial();
void configurar_pines();
void configurar_mpu6050();

// Funciones de operación
void verificarBoton();
void calibrarMPU();
void leerYMostrarDatosMPU();

#endif