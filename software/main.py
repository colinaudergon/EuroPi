from machine import Pin, Timer, ADC
import time
import tm1637
import micropython
import _thread
import machine
import gc
gc.enable()

mydisplay = tm1637.TM1637(clk=Pin(26), dio=Pin(27))

led=Pin(19,Pin.OUT)

adc = ADC(Pin(28))

tempo=1490
tempo_2=20
bpm=0
bpm_old=0


def interruption_handler(timer):
    led.value(1)
    soft_timer_2 = Timer(mode=Timer.ONE_SHOT , period=tempo_2, callback=interruption_handler_2)
    #update_time()
    soft_timer.init(period=int(tempo), callback=interruption_handler)
    
def interruption_handler_2(timer):   
    led.value(0)
    
    
    
    
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

    
def adc_reader(timer):
    global bpm
    global tempo
    global bpm_old
    tempo = int(translate(int(adc.read_u16()),352,65535,300,1490))
    bpm=(60 * 1000) /tempo
    
    if(bpm != bpm_old):
            mydisplay.number(int(bpm))
            mydisplay.show(" ")
            bpm_old= bpm
    

adc_timer = Timer(mode=Timer.PERIODIC, period=200, callback=adc_reader)
soft_timer = Timer(mode=Timer.PERIODIC, period=int(tempo), callback=interruption_handler)

while True:
    pass

        
        

