from machine import Pin, PWM
from time import sleep_ms

IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
ENA = PWM(Pin(4))
ENA.freq(1000)

IN1.value(0)
IN2.value(0)
#ENA.duty_u16(65535)

def set_speed(percent):
  percent = max(0, min(100, percent))
  duty = int(percent * 65535 / 100)
  ENA.duty_u16(duty)

def forward():
  IN1.value(1)
  IN2.value(0)

def reverse():
  IN1.value(0)
  IN2.value(1)

def stop():
  IN1.value(0)
  IN2.value(0)

def ramp_to(start, end, step = 10, delay_ms = 100):

  if end > 100:
    print("Te pasaste")
    end = 101

  if start < 0:
    print("Te falto")
    start = -1

  if end < 0:
    print("Te falto")
    end = -1

  if start > 100:
    print("Te pasaste")
    start = 101

  if start <= end:
    for speed in range (start, end, step):
      set_speed(speed)
      if speed == -1:
        speed = 0
      print("Velocidad: ", speed, "%")
      sleep_ms(delay_ms)
    
  else: 
    for speed in range (start, end, -step):
      set_speed(speed)
      if speed == -1:
        speed = 0
      print("Velocidad: ", speed, "%")
      sleep_ms(delay_ms)

stop()
sleep_ms(1000)

while True:

  forward()
  sleep_ms(2000)
  ramp_to(0, 100)
  ramp_to(100, 0)
  sleep_ms(2000)
  reverse()
  ramp_to(0, 75)
  ramp_to(75, 0)
  sleep_ms(2000)
  stop()




