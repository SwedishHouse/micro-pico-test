from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print('Average  of two numbers')
pin.value(1)
n1 = float(input('First num: '))
pin.value(0)
n2 = float(input('Second num: '))

print('Average: ', (n1 + n2)/2)
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
