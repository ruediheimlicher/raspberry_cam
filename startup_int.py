#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# neu GPIO23 (Port16) als Eingang fuer IN/OUT-Taste
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# zaehler fuer falling edge
edgecount=0
last_counttime=TIME.time()
global last_clicktime
last_clicktime=TIME.time()
print("last: ",int(last_clicktime))

def on_off_callback(channels):
	print("Falling Edge")
	import time as TIME	
	global edgecount
	global last_clicktime
	clicktime=TIME.time()
	print("clicktime: ",int(clicktime), " last: ",int(last_clicktime), "diff: ",int(clicktime-last_clicktime))
	#subprocess.call(['sudo','reboot'])
	if ((clicktime-last_clicktime)>5):	# timeout, edgecount reset
		print("edgecount reset",edgecount, "last: ",int(last_clicktime))
		edgecount=0
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



print("add event detect")
#
#GPIO.add_event_detect(24,GPIO.FALLING, callback=on_off_callback, bouncetime=200)

# neu GPIO23 als Eingang fuer ON/OFF
GPIO.add_event_detect(23,GPIO.FALLING, callback=on_off_callback, bouncetime=200)
#GPIO.add_event_callback(24,on_off_callback)

#lasttime=TIME.time()
#while (True):
while (True):	
	akttime=TIME.time()
	if (akttime-last_counttime>2):
		print("**",int(akttime), " last: ",int(last_counttime))
		last_counttime=akttime	
		#pass
print("cleanup")
#GPIO.cleanup()
