#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.output(16,1)
i=0
while (i<4):
	print (i)
	GPIO.output(16,0)
	TIME.sleep(1)
	GPIO.output(16,1)
	TIME.sleep(1)

	i= i+1
GPIO.output(16,0)

