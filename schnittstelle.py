#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.VERSION
print ('Version: ',GPIO.VERSION)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,1)
i=0
while (i<4):
	print (i)
	GPIO.output(8,0)
	TIME.sleep(1)
	GPIO.output(8,1)
	TIME.sleep(1)

	i= i+1

GPIO.setup(12,GPIO.OUT)
#GPIO.output(12,0)
#i=0
#while (i<3):
#	print (i)
#	GPIO.output(12,1)
#	TIME.sleep(1)
#	GPIO.output(12,0)
#	TIME.sleep(1)
#	i= i+1

GPIO.output(12,1)
