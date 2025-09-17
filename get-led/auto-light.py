import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=26
GPIO.setup(led,GPIO.OUT)
pt=6
GPIO.setup(pt,GPIO.IN)
state=0
while True:
    state = not (GPIO.input(pt))
    GPIO.output(led, state)

