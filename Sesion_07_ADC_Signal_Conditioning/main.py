from machine import Pin, ADC
from time import sleep_ms

# Entradas y salidas
sensor = ADC(Pin(26))
green = Pin(13, Pin.OUT)
yellow = Pin(14, Pin.OUT)
red = Pin(15, Pin.OUT)

# Configuracion
WARNING = 50
ALARM = 75
N = 10
SAMPLE_MS = 100

lecturas = []

while True:
    # Leer sensor
    raw = sensor.read_u16()

    # Promedio movil
    lecturas.append(raw)

    if len(lecturas) > N:
        lecturas.pop(0)

    promedio = sum(lecturas) / len(lecturas)

    # Conversiones
    voltaje = promedio * 3.3 / 65535
    porcentaje = promedio * 100 / 65535

    # Estado
    if porcentaje >= ALARM:
        estado = "ALARM"
        green.value(0)
        yellow.value(0)
        red.value(1)

    elif porcentaje >= WARNING:
        estado = "WARNING"
        green.value(0)
        yellow.value(1)
        red.value(0)

    else:
        estado = "NORMAL"
        green.value(1)
        yellow.value(0)
        red.value(0)

    # Mostrar informacion
    print(
        "Raw:", raw,
        "| Voltaje:", round(voltaje, 2),
        "| Porcentaje:", round(porcentaje, 1),
        "| Estado:", estado
    )

    sleep_ms(SAMPLE_MS)
