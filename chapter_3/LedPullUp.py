from machine import Pin
import utime

Blue = Pin(0, Pin.OUT, pull = Pin.PULL_DOWN)
RED = Pin(1, Pin.OUT, pull = Pin.PULL_DOWN)
GREEN = Pin(2, Pin.OUT, pull = Pin.PULL_DOWN)

values = [[r, g, b] for r in range(3) for g in range(3) for b in range(3)]

counter = 0
max_length = len(values)

while True:
    RED.value(values[counter][0])
    GREEN.value(values[counter][1])
    Blue.value(values[counter][2]) 
    utime.sleep(1)
    counter += 1
    counter %= max_length
    # Blue.value(1)
    # RED.value(1)
    # GREEN.value(1)
    # utime.sleep(1)
    
Blue.off()
RED.off()
GREEN.off()
print("Finished.")