#include "funciones.h"

void setup() {
  iniciar_comunicacion_serial();
  configurar_pines();
  configurar_mpu6050();
}

void loop() {
  //verificarBoton();
  if (calibracionSolicitada) {
    calibrarMPU();
    calibracionSolicitada = false;
  }
  if (!dmpListo) return;
  leerYMostrarDatosMPU();

}