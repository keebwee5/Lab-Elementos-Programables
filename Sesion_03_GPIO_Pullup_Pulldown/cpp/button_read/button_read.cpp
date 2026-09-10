#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    stdio_init_all();

    const uint BUTTON_PIN = 16;

    gpio_init(BUTTON_PIN);
    gpio_set_dir(BUTTON_PIN, GPIO_IN);
    gpio_pull_up(BUTTON_PIN);

    while (true) {
        printf("%d\n", gpio_get(BUTTON_PIN));
        sleep_ms(200);
    }

    return 0;
}
