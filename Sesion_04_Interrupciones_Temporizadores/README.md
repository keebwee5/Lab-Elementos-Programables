# Sesión 04: Interrupciones y Temporizadores (Timers)

### 1. Objetivo
Implementar y comprender el uso de eventos asíncronos en microcontroladores utilizando interrupciones de hardware y temporizadores, evitando el uso de demoras bloqueantes (`sleep`). Se aplicarán estos conceptos para crear un "Juego de los Reflejos".

### 2. Circuito
*   **Hardware Principal:** Raspberry Pi Pico (Simulación en Wokwi) y Raspberry Pi Pico 2 W (Implementación física para el juego).
*   **Componentes:**
    *   1x LED Naranja (Señal visual / Señal de espera) conectado al GP15.
    *   1x LED Rosa (Señal de espera / Señal visual) conectado al GP14.
    *   1x Botón pulsador conectado al GP16.
    *   Resistencias adecuadas para los LEDs y configuración de resistencia Pull-Up interna para el botón.

### 3. Qué es una interrupción
Una interrupción (IRQ) es una señal que detiene momentáneamente la ejecución del programa principal (`while True`) para atender un evento urgente generado por el hardware (como presionar un botón). Una vez que la interrupción ejecuta su función asignada (callback), el programa principal retoma su ejecución desde donde se pausó. Esto permite reaccionar a eventos físicos de manera casi instantánea.

### 4. Qué es un temporizador
Un temporizador (Timer) es un periférico de hardware que cuenta el tiempo de forma independiente al procesador principal. Permite programar la ejecución de una función (callback) después de que haya transcurrido un tiempo específico, ya sea una sola vez (modo `ONE_SHOT`) o de manera repetitiva (periódica). A diferencia de los comandos como `sleep`, los temporizadores no bloquean la ejecución del resto del código.

### 5. Resultados en ms
*(Aquí debes colocar los resultados reales que obtuviste al jugar. Te dejo un ejemplo de cómo llenarlo)*
*   **Intento 1:** 245 ms
*   **Intento 2:** 210 ms
*   **Intento 3:** 280 ms
*   *(Nota: Ocasionalmente se registraron "SALIDAS EN FALSE" al presionar el botón antes de la señal del LED).*

### 6. Problemas encontrados
*(Ajusta esta sección según tu experiencia real en el laboratorio. Te dejo los problemas más comunes en esta práctica)*
*   **Ruido en el botón (Rebotes):** Al presionar el botón físicamente, el microcontrolador detectaba múltiples pulsaciones rápidas debido al ruido mecánico del interruptor. Se solucionó implementando un *debounce* por software, ignorando cualquier interrupción que ocurriera con menos de 80 ms de diferencia respecto a la anterior.
*   **Variables globales:** Hubo dificultades iniciales al intentar modificar variables dentro de las funciones *callback* de las interrupciones y temporizadores, lo cual se resolvió asegurando el uso de la palabra clave `global` en Python.

### 7. Conclusión
El uso de interrupciones y temporizadores es fundamental para desarrollar sistemas embebidos eficientes y reactivos. A diferencia de la programación secuencial tradicional, el diseño basado en eventos permite que el microcontrolador realice múltiples tareas en segundo plano mientras está alerta a cambios en su entorno, optimizando el uso de los recursos de hardware y mejorando significativamente los tiempos de respuesta.