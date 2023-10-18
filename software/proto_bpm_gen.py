from machine import Pin,Timer, ADC

led = Pin(21, Pin.OUT)
#adc = ADC(Pin(26))

i=0
time=1490
time_2=20

def interruption_handler(timer):
    led.value(1)
    soft_timer_2 = Timer(mode=Timer.ONE_SHOT , period=time_2, callback=interruption_handler_2)
    #update_time()
    #soft_timer.init(period=time, callback=interruption_handler)
    
def interruption_handler_2(timer):   
    led.value(0)
    
def BPM_Printer():
    global time
    #converstion between time and BPM 
    bpm=(60*1000)/time
    print("BPM: " + str(bpm))

def update_time():
    global time
    # read ADC value and update time accordingly
    adc_value = adc.read()
    time = 1000 + adc_value * 10


if __name__ == "__main__":
    #global time
    soft_timer = Timer(mode=Timer.PERIODIC, period=time, callback=interruption_handler)
    #while True:
    #    BPM_Printer()



