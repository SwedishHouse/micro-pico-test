from machine import Pin
from utime import sleep
import math

pin = Pin("LED", Pin.OUT)
pin.value(1)
print('Surface area of cylinder')
r = float(input('Enter radius:'))
h = float(input('Enter height:'))

print(f'Surface area = {2 * math.pi * r *h}')
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")

