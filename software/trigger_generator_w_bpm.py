from machine import Pin, Timer, ADC
import time

a = Pin(1, Pin.OUT)
b = Pin(2, Pin.OUT)
c = Pin(3, Pin.OUT)
d = Pin(4, Pin.OUT)
e = Pin(5, Pin.OUT)
f = Pin(6, Pin.OUT)
g = Pin(7, Pin.OUT)

select_1=Pin(16, Pin.OUT)
select_2=Pin(17, Pin.OUT)
select_3=Pin(18, Pin.OUT)

led=Pin(19,Pin.OUT)

led_pin=[a, b, c, d, e, f, g]

select=[select_1,select_2,select_3]

adc = ADC(Pin(28))

tempo=1490
tempo_2=20

def zero():
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)
    e.value(0)
    f.value(0)

def one():
    b.value(0)
    c.value(0)

def two():
    a.value(0)
    b.value(0)
    d.value(0)
    e.value(0)
    g.value(0)

def three():
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)
    g.value(0)

def four():
    b.value(0)
    c.value(0)
    f.value(0)
    g.value(0)

def five():
    a.value(0)
    c.value(0)
    d.value(0)
    f.value(0)
    g.value(0)

def six():
    a.value(0)
    c.value(0)
    d.value(0)
    e.value(0)
    f.value(0)
    g.value(0)

def seven():
    a.value(0)
    b.value(0)
    c.value(0)

def eight():
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)
    e.value(0)
    f.value(0)
    g.value(0)

def nine():
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(0)
    f.value(0)
    g.value(0)

        
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

def BPM_Printer():
    global tempo
    # Convert time to BPM
    bpm = (60 * 1000) / tempo
    print("BPM: " + str(bpm))
    #display_bpm(bpm)
    
    hundreds = int(bpm) // 100
    tens = (int(bpm) // 10) % 10
    units = int(bpm) % 10
    digit=[hundreds, tens, units]
    i=0

    for pin in select:
        if(i<3):
            a.value(1)
            b.value(1)
            c.value(1)
            d.value(1)
            e.value(1)
            f.value(1)
            g.value(1)
            pin.value(1)
            value_tester(digit[i])
            time.sleep(0.001)  # delay to avoid ghosting
            pin.value(0)
            i=i+1
        else:
            i=0

        
def value_tester(digit):
    if digit == 0:
        zero()
    elif digit == 1:
        one()
    elif digit == 2:
        two()
    elif digit == 3:
        three()
    elif digit == 4:
        four()
    elif digit == 5:
        five()
    elif digit == 6:
        six()
    elif digit == 7:
        seven()
    elif digit == 8:
        eight()
    elif digit == 9:
        nine()

def adc_reader(timer):
    global tempo
    adc_value = int(translate(int(adc.read_u16()),352,65535,300,1490))#
    tempo=adc_value
    
soft_timer = Timer(mode=Timer.PERIODIC, period=int(tempo), callback=interruption_handler)
adc_timer = Timer(mode=Timer.PERIODIC, period=110, callback=adc_reader)

while True:
    
    BPM_Printer()
    
        
        
