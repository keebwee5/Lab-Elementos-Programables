from time import sleep_ms
from machine import Pin

CAR_R = 15
CAR_Y = 14
CAR_G = 13
PED_R = 12
PED_G = 11
BUTTON = 16

car_red = Pin(CAR_R, Pin.OUT)
car_yellow = Pin(CAR_Y, Pin.OUT)
car_green = Pin(CAR_G, Pin.OUT)
ped_red = Pin(PED_R, Pin.OUT)
ped_green = Pin(PED_G, Pin.OUT)
button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

def set_lights(car_r, car_y, car_g, ped_r, ped_g):
    car_red.value(car_r)
    car_yellow.value(car_y)
    car_green.value(car_g)
    ped_red.value(ped_r)
    ped_green.value(ped_g)
    

def cars_go():
    print("S0 REPOSO: Autos pasan, peanton espera")
    set_lights(0, 0, 1, 1, 0)

def cars_transition():
    print("S1 TRANCISION: Autons preparan alto")
    set_lights(0, 1, 0, 1, 0)

def pedestrians_go():
    print("S2 CRUCE: Peaton puede pasar")
    set_lights(1, 0, 0, 0, 1)

def pedestrians_finish():
    print("S3 FIN DE CRUCE: peaton verde parpadea")
    set_lights(1, 0, 0, 0, 1)

    for _ in range(6):
        ped_green.toggle()
        sleep_ms(300)
    ped_green.value(0)
    ped_red.value(1)

def crossing_sequence():
    cars_transition()
    sleep_ms(1500)

    pedestrians_go()
    sleep_ms(4000)

    pedestrians_finish()
    sleep_ms(500)

    cars_go()

cars_go()
last = 1

while True:
    now = button.value()
    
    if last == 1 and now == 0:
        sleep_ms(30)
        
        if button.value() == 0:
            print("Peticion peatonal !!")
            crossing_sequence()

            while button.value() == 0:
                sleep_ms(10)

    last == now
    sleep_ms(10)
    
