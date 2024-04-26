#single led
import RPi.GPIO as GPIO
import time
GPIO.Setmode(GPIO.BCM)
GPIO.Setworning(False)
time sleep(1)
GPIO.Setup(14,GPIO.OUT);
GPIO.Output(14,True)
time sleep(1)
GPIO.Output(14,False)
