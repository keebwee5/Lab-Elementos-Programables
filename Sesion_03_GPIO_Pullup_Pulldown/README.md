#  Semáforo Peatonal y Entradas Digitales (Raspberry Pi Pico)

Este proyecto contiene las prácticas correspondientes a la configuración de pines GPIO como entradas digitales en la Raspberry Pi Pico. El objetivo final es controlar la secuencia de un semáforo interactivo mediante un botón físico.

##  Contenido del proyecto

* **`01_button_read`**: Ejercicio básico para leer el estado lógico de un botón implementando resistencias pull-up/pull-down.
* **`02_button_debounce`**: Implementación de una rutina antirrebote (*debounce*) por software para evitar lecturas múltiples falsas al presionar el botón.
* **`03_semaforo_peatonal`**: Práctica final que integra la lectura validada del botón para interrumpir el estado de reposo de los LEDs y activar la secuencia de un cruce peatonal seguro.
