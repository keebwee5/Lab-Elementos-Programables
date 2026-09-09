from machine import Pin
from time import sleep_ms

button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())
    sleep_ms(200)

    
