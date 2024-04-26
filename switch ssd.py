#switch ssd
import RPi.GPIOas GPIO
import time
GPIO.Setmode(GPIO.BCM)
GPIO.Setwornings(False)
time.sleep(1)
sw1=20
a=14
b=15
c=18
d=23
e=24
f=25
g=8
dp=7
GPIO.Setup(a,GPIO.OUT)
GPIO.Setup(b,GPIO.OUT)
GPIO.Setup(c,GPIO.OUT)
GPIO.Setup(d,GPIO.OUT)
GPIO.Setup(e,GPIO.OUT)
GPIO.Setup(f,GPIO.OUT)
GPIO.Setup(g,GPIO.OUT)
GPIO.Setup(dp,GPIO.OUT)
GPIO.Setup(sw1,GPIO.IN)
while True:
    if(GPIO.INPUT(sw1)):
        GPIO.OUTPUT(a,False)
        GPIO.OUTPUT(b,False)
        GPIO.OUTPUT(c,False)
        GPIO.OUTPUT(d,False)
        GPIO.OUTPUT(e,False)
        GPIO.OUTPUT(f,False)
        GPIO.OUTPUT(g,True)
        GPIO.OUTPUT(dp,True)
    else:
        GPIO.OUTPUT(a,True)
        GPIO.OUTPUT(b,False)
        GPIO.OUTPUT(c,False)
        GPIO.OUTPUT(d,True)
        GPIO.OUTPUT(e,True)
        GPIO.OUTPUT(f,True)
        GPIO.OUTPUT(g,True)
        GPIO.OUTPUT(dp,True)
