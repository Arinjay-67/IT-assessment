from machine import Pin, PWM 

from time import sleep 

  

led = Pin(15, Pin.OUT) 

  

while True: 

    led.value(0) 

    sleep() 

    led.value(0) 

    sleep(1) 

    led.value(100) 