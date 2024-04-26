#switch one led
import RPi.GPIO as GPIO
import time
GPIO.Setmode(GPIO.BCM)
GPIO.Setwornings(False)
l1=14
sw1=20
GPIO.Setup(l1,GPIO.OUT)
GPIO.Setup(sw1,GPIO.IN)
while True:
    if(GPIO.INPUT(sw1)):
        GPIO.OUTPUT(l1,True)
    else:
        GPIO.OUTPUT(l1,False)
 
