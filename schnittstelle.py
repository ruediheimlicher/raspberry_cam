#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.VERSION
print ('Version: ',GPIO.VERSION)
GPIO.setup(8,GPIO.OUT)
i=0
while (i<10):
	print (i)
	GPIO.output(8,1)
	TIME.sleep(1)
	GPIO.output(8,0)
	TIME.sleep(1)
	i= i+1
