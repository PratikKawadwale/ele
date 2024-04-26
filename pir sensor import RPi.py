#pir sensor
import RPi.GPIO as GPIO
import time
GPIO.Setmode(GPIO.BCM)
GPIO.Setwornings(False)
time.sleep(1)
pir=23
l1=24
buzzer=25
GPIO.Setup(pir, GPIO.IN)
GPIO.Setup(l1, GPIO.OUT)
GPIO.Setup(buzzer, GPIO.OUT)
while True:
    val=pir
    print(val)
    if(val==True):
        GPIO.OUTPUT(l1,True)
        GPIO.OUTPUT(buzzer,True)
    else:
        GPIO.OUTPUT(l1,False)
        GPIO.OUTPUT(buzzer,False)
        
