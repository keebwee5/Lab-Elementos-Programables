#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"

const uint32_t flash_const = 0x12345678;
uint32_t global conter = 0;

int main() {
  stdio_init_all();
  sleep_ms(3000);

  uint32_t stack_value - 0xABCDEF01;
  uint8_t *heap_buffer = malloc(1024);

  printf("flash const:  %p\n", &flash_const);
  printf("global:  %p\n", &global_counter);
  printf("flash const:  %p\n", &stack_value);
  printf("heap ptr:  %p\n", &heap_buffer);
}
