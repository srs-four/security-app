import send
from send import sendr
import RPi.GPIO as GPIO
import time
from gpiozero import LED, Button
from signal import pause

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

#while True:
def notify():
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders")
        sendr()
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected")

notify()
#button = Button(4)
#button.when_pressed = notify