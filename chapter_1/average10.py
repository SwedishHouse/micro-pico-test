from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print('Average  of 10 numbers')
pin.value(1)
value = 0
for i in range(10):
    value += float(input(f'Num {i}: '))
    pin.toggle()

print('Average: ', value/10)
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")