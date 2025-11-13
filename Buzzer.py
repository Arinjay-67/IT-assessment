from machine import Pin 

import time 

  

buzzer = Pin(11, Pin.OUT) 

  

while True: 

    buzzer.value(1) 

 

 

from machine import Pin, PWM, ADC 

import time 

  

  

buzzer = PWM(Pin(11))   

pot = ADC(26)          

  

while True: 

    value = pot.read_u16()                

    freq = int(200 + (value / 65535) * 3000)   

    buzzer.freq(freq)                      

    buzzer.duty_u16(40000)           

    time.sleep(0.05) 

 