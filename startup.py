#!/usr/bin/python3
import RPi.GPIO as GPIO
import time as TIME
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# zaehler fuer falling edge
edgecount=0
def on_off_callback(kanal):
	print("Falling Edge")
	#Test:Blinky einschalten, Port 12 LO
	GPIO.setup(12,GPIO.OUT)
	GPIO.output(12,1)

# Port 16 als Input

# event-detect config
#GPIO.add_event_detect(16,GPIO.FALLING,callback=on_off_callback, bouncetime=200)

lastklickzeit=TIME.time()*1000
print("lastklickzeit: ",lastklickzeit)

# Warten auf Ecke
while (edgecount<4):
	try:
		print("Warten auf Falling")
		GPIO.wait_for_edge(16,GPIO.FALLING)
		print("Falling bemerkt")
		klickzeit=TIME.time()*1000
		if ((klickzeit-lastklickzeit)>5000):
			edgecount=0
			lastklickzeit=klickzeit
		if (edgecount<2):
			print ("Anzahl: ",edgecount)
			edgecount=edgecount+1
		else:
			print("3 Fallings bemerkt")
			GPIO.setup(12,GPIO.OUT)
			GPIO.output(12,1)
			subprocess.call(['pkill','raspivid'])
			subprocess.call(['sudo','halt'])
	except KeyboardInterrupt:
		print("Keyboard Input")

