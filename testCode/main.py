from machine import Pin
import time

if __name__=='__main__':
    led = Pin(2, Pin.OUT)
    while True:
        led.toggle()
        time.sleep(1)
