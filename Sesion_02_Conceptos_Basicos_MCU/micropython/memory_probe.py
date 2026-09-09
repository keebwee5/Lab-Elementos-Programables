import time
time.sleep(0.1)

import os, gc, machine

print(os.uname())
print('frecuencia: ', machine.freq())

gc.collect()
print('Libre inicial: ', gc.mem_free())

buffer = bytearray(20000)
print('despues de reservar: ', gc.mem_free())

del buffer 
gc.collect()
print('despues de liberar: ', gc.mem_free())