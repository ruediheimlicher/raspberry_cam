#!/usr/bin/env python3
import subprocess
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
print ("camera_GPIO")
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,0)
i=0
while (i<4):
	print (i)
	GPIO.output(8,1)
	TIME.sleep(0.5)
	GPIO.output(8,0)
	TIME.sleep(0.5)
	i=i+1
GPIO.output(8,1)
#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
#subprocess.call(['raspivid','--preview','-80,0,800,480','-t','0','-fps','30','-roi','0,0.125,0.99,0.85'])
