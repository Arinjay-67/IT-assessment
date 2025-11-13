from machine import Pin, PWM, ADC 

from time import sleep 

button = Pin(14, Pin.IN, Pin.PULL_DOWN) 

buzzer = PWM(Pin(15)) 

pot = ADC(26) 

led_brightness = PWM(Pin(16)) 

led_brightness.freq(1000) 

  

rgb = [PWM(Pin(p)) for p in (17, 18, 19)] 

for led in rgb: 

    led.freq(1000) 

def pot_to_rgb(value): seg, rem = divmod(value, 21845) max_val = 65535 if seg == 0: return (max_val - rem * max_val // 21845, rem * max_val // 21845, 0) if seg == 1: return (0, max_val - rem * max_val // 21845, rem * max_val // 21845) return (rem * max_val // 21845, 0, max_val - rem * max_val // 21845) 

while True: val = pot.read_u16() 

if button.value(): 
    buzzer.freq(200 + val * 1800 // 65535) 
    buzzer.duty_u16(30000) 
    led_brightness.duty_u16(val) 
    r, g, b = pot_to_rgb(val) 
    rgb[0].duty_u16(r) 
    rgb[1].duty_u16(g) 
    rgb[2].duty_u16(b) 
else: 
    buzzer.duty_u16(0) 
    led_brightness.duty_u16(0) 
    for led in rgb: 
        led.duty_u16(0) 
 
sleep(0.05)