#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#GPIO.remove_event_detect(25)

# zaehler fuer falling edge
edgecount=0
last_clicktime=TIME.time()

def on_off_callback(channels):
	print("Falling Edge")
	import time as TIME	
	global edgecount
	global last_clicktime
	clicktime=TIME.time()
	#subprocess.call(['sudo','reboot'])
	if ((clicktime-last_clicktime)>5):	# timeout, edgecount reset
		edgcount=0
		last_clicktime=clicktime
	
	if (edgecount<2):
		print("Anzahl: ",edgecount)
		edgecount=edgecount+1
	else:
		print("Dritter Click")
		GPIO.setup(18,GPIO.OUT) # Port 12
		GPIO.output(18,1)
		
		subprocess.call(['pkill','raspivid'])	
		subprocess.call(['sudo','reboot'])
		GPIO.cleanup()


#	subprocess.call(['pkill','raspivid'])
	#Test:Blinky einschalten, Port 12 LO
#	GPIO.setup(25,GPIO.OUT)
#	GPIO.output(25,1)

# Port GPIO24 (Port 18) als Input

# event-detect config
print("add event detect")
GPIO.add_event_detect(24,GPIO.FALLING, callback=on_off_callback, bouncetime=200)
#GPIO.add_event_callback(24,on_off_callback)

#lasttime=TIME.time()
#while (True):
while (True):	
	akttime=TIME.time()
	if (akttime-last_clicktime>2):
		print("**",int(akttime))
		last_clicktime=akttime	
		#pass
print("cleanup")
#GPIO.cleanup()
