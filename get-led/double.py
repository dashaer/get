import RPi.GPIO as GPIO
import time
def binNum(n):
    return[int(e) for e in bin(n)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds=list(reversed([24,22,23,27,17,25,12,16]))
# print(*leds)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup([9,10],GPIO.IN)
sleepTime=0.2

arrowUp=9
arrowDown=10

for i in leds:
    GPIO.output(i,0)

n=0
while True:
    if (GPIO.input(arrowUp)>0 and GPIO.input(arrowDown)>0): #or (GPIO.input(arrowDown)>0 and GPIO.input(arrowUp)>0):
        n=255
        Bn=binNum(n)
        time.sleep(sleepTime+0.5)
        for i in range(8):
            GPIO.output(leds[i],Bn[i])


        
    elif GPIO.input(arrowUp)>0:
        if n<255:    
            n+=1
            Bn=binNum(n)
            print(n,Bn)
            time.sleep(sleepTime)
        for i in range(8):
            GPIO.output(leds[i],Bn[i])

    elif GPIO.input(arrowDown)>0:
        if n>0:
            n-=1
            Bn=binNum(n)
            print(n,Bn)
            time.sleep(sleepTime)

        for i in range(8):
            GPIO.output(leds[i],Bn[i])
