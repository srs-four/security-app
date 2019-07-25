from send import sendr
import RPi.GPIO as GPIO
import time
from gpiozero import LED, Button
from signal import pause
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)   


led = LED(12)
button = Button(4)
i=GPIO.input(11)

class security:
    def __init__(self,led):
        self.led = led

    def armed(self):
        print("system on")
        sleep(5)
        if i== False:
            print(".....")
            sleep(0.5)
            led.on()
            print ("motion detected...")
            #sendr()
        elif i== True:               
            print ("no intruder")
    def off(self):
        print("system off")
        led.off()


system = security(led)
x=0
try:
    
    print("System ready")
    while True:
        sleep(3)
        x+=1
        if ((x%2)== True):
            button.when_pressed = system.armed
            
        elif ((x%2) == False):
            button.when_pressed = system.off
        
        print("Cycle ", x)
        sleep(20)
        
            
except():
    GPIO.cleanup()


