#single led blinking
import RPi.GPIO as GPIO
import time
GPIO.Setmode(GPIO.BCM)
GPIO.Setwornings(False)
time.sleep(1)
GPIO.Setup(14,GPIO.OUT)
while True:
    GPIO.Output(14,True)
    time.sleep(0.5)
    GPIO.Output(14,False)
    time.sleep(0.5)
