#4 led on/off
import RPi.GPIO as GPIO
import time
GPIO.Setmode(GPIO.BCM)
GPIO.Setwornings(False)
l1=14
l2=15
l3=18
l4=23
time.sleep(1)
GPIO.Setup(l1,GPIO.OUT)
GPIO.Setup(l2,GPIO.OUT)
GPIO.Setup(l3,GPIO.OUT)
GPIO.Setup(l4,GPIO.OUT)
time.sleep(1)
GPIO.Output(l1,True)
GPIO.Output(l2,True)
GPIO.Output(l1,False)
GPIO.Output(l2,False)
GPIO.Output(l3,True)
GPIO.Output(l4,True)
GPIO.Output(l3,False)
GPIO.Output(l4,False)
