from send.py import sendr
from gpiozero import Button
from signal import pause

button = Button(2)

def buttonpress():
    print('Test in progress')
    sendr()

button.when_pressed = buttonpress

pause()


