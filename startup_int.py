#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Wird in gpio.sh aufgerufen (beim Start in rc.local)
# Setzt GPIO23 (Port16) als Eingang fuer Taste. 
# Laeuft im Hintergrund.
# Anschliessend wird camera_full.py von gpio.sh  aufgerufen


# neu GPIO23 (Port16) als Eingang fuer IN/OUT-Taste
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# zaehler fuer falling edge
edgecount=0

# aktuelle Zeit lesen
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

	if ((clicktime-last_clicktime)>5):	# timeout, edgecount reset
		print("edgecount reset",edgecount, "last: ",int(last_clicktime))
		edgecount=0
		last_clicktime=clicktime # last auf aktuelle Zeit setzen
	
	if (edgecount<2): # edgecount incrementieren
		print("Anzahl: ",edgecount)
		edgecount=edgecount+1
	else: # ernst gemeint, 3 Clicks, ausschalten einleiten
		print("Dritter Click")

		# Anzeige Camera reset
		GPIO.setup(15, GPIO.OUT) # Port 10
		GPIO.output(15,0)
		
		# Anzeige Camera an Monitor OFF
		GPIO.setup(25,GPIO.OUT)
		GPIO.output(25,0)

		# Camera off
		subprocess.call(['pkill','raspivid'])	

		# kurz warten
		TIME.sleep(3)
		
		# Anzeige Status reset
		GPIO.setup(18,GPIO.OUT) # Port 12
		GPIO.output(18,1)
		
		GPIO.cleanup()
		# Raspi off		
		subprocess.call(['sudo','shutdown','-h','0'])



print("add event detect")
#

# neu GPIO23 als Eingang fuer ON/OFF
GPIO.add_event_detect(23,GPIO.FALLING, callback=on_off_callback, bouncetime=200)

while (True):	
	akttime=TIME.time()
	if (akttime-last_counttime>2):
		print("**",int(akttime), " last: ",int(last_counttime))
		last_counttime=akttime	
		#pass
print("cleanup")
#GPIO.cleanup()
