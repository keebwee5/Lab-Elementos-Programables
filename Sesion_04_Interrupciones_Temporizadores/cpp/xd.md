// Sesion 04 - Juego de reflejos en C/C++ para Raspberry Pi Pico SDK
// Circuito:
//   GP15 -> LED verde de señal -> GND
//   GP14 -> LED amarillo de espera -> GND
//   GP16 -> boton -> GND con pull-up interno
 
#include <stdio.h>
#include <stdlib.h>
#include "pico/stdlib.h"
#include "pico/time.h"
#include "hardware/gpio.h"
 
#define LED_SIGNAL 15
#define LED_WAIT   14
#define BUTTON     16
 
#define STATE_WAITING 0
#define STATE_READY   1
#define STATE_DONE    2
 
volatile uint8_t state = STATE_DONE;
volatile uint32_t start_ms = 0;
volatile uint32_t reaction_ms = 0;
volatile uint32_t last_irq_ms = 0;
volatile bool result_ready = false;
volatile bool false_start = false;
volatile alarm_id_t active_alarm = 0;
uint32_t round_number = 0;
 
static inline uint32_t now_ms(void) {
    return to_ms_since_boot(get_absolute_time());
}
 
int64_t show_signal(alarm_id_t id, void *user_data) {
    gpio_put(LED_SIGNAL, 1);
    gpio_put(LED_WAIT, 0);
    start_ms = now_ms();
    state = STATE_READY;
    return 0; // one-shot: no repetir
}
 
void schedule_round(void) {
    round_number++;
    gpio_put(LED_SIGNAL, 0);
    gpio_put(LED_WAIT, 1);
 
    result_ready = false;
    false_start = false;
    state = STATE_WAITING;
 
    uint32_t delay_ms = 1000 + (now_ms() % 4000);
 
    printf("\n==============================\n");
    printf("Ronda %lu\n", (unsigned long)round_number);
    printf("Espera la senal visual. No presiones antes.\n");
    printf("Delay pseudoaleatorio: %lu ms\n", (unsigned long)delay_ms);
    printf("==============================\n");
 
    active_alarm = add_alarm_in_ms(delay_ms, show_signal, NULL, false);
}
 
void gpio_callback(uint gpio, uint32_t events) {
    if (gpio != BUTTON) return;
    if (!(events & GPIO_IRQ_EDGE_FALL)) return;
 
    uint32_t now = now_ms();
 
    // Debounce simple
    if ((uint32_t)(now - last_irq_ms) < 80) return;
    last_irq_ms = now;
 
    if (state == STATE_READY) {
        reaction_ms = now - start_ms;
        gpio_put(LED_SIGNAL, 0);
        result_ready = true;
        state = STATE_DONE;
    }
    else if (state == STATE_WAITING) {
        if (active_alarm > 0) {
            cancel_alarm(active_alarm);
            active_alarm = 0;
        }
        false_start = true;
        result_ready = true;
        state = STATE_DONE;
    }
}
 
int main() {
    stdio_init_all();
    sleep_ms(2000);
 
    gpio_init(LED_SIGNAL);
    gpio_set_dir(LED_SIGNAL, GPIO_OUT);
 
    gpio_init(LED_WAIT);
    gpio_set_dir(LED_WAIT, GPIO_OUT);
 
    gpio_init(BUTTON);
    gpio_set_dir(BUTTON, GPIO_IN);
    gpio_pull_up(BUTTON);
 
    gpio_set_irq_enabled_with_callback(BUTTON, GPIO_IRQ_EDGE_FALL, true, &gpio_callback);
 
    printf("Sesion 04 - Juego de reflejos C/C++\n");
    printf("Pull-up: reposo = 1, presionado = 0\n");
 
    schedule_round();
 
    while (true) {
        if (result_ready) {
            if (false_start) {
                printf("SALIDA FALSA: presionaste antes de la senal\n");
            } else {
                printf("Tiempo de reaccion: %lu ms\n", (unsigned long)reaction_ms);
            }
 
            sleep_ms(1800);
 
            // Esperar a que el usuario libere el boton antes de nueva ronda
            while (gpio_get(BUTTON) == 0) {
                sleep_ms(10);
            }
 
            schedule_round();
        }
 
        tight_loop_contents();
    }
}
 
