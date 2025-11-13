from machine import ADC, Pin, PWM 

from time import sleep 

  

  

pot = ADC(26)   

  

  

led = PWM(Pin(15))   

led.freq(1000)       

  

while True: 

     

    value = pot.read_u16()   

    print(value)             

     

  

    duty = int(value / 65535 * 65535) 

    led.duty_u16(duty)       

     

    sleep(0.1) 