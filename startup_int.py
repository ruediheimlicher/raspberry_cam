#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.remove_event_detect(25)

# zaehler fuer falling edge
edgecount=0
def on_off_callback(channels):
	print("Falling Edge")
	#Test:Blinky einschalten, Port 12 LO
#	GPIO.setup(25,GPIO.OUT)
#	GPIO.output(25,1)

# Port 18 als Input

# event-detect config
print("add event detect")
GPIO.add_event_detect(25,GPIO.FALLING, bouncetime=2)
GPIO.add_event_callback(25,on_off_callback)

#GPIO.wait_for_edge(25,GPIO.RISING)

while (True):
	pass
GPIO.cleanup()
