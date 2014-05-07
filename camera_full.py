#!/usr/bin/env python3
import subprocess
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
print ("camera_full")
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,0)

#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
subprocess.call(['raspivid','--preview','-80,0,800,480','-t','0','-fps','30','-roi','0,0.125,0.99,0.85'])

#subprocess.call(['sudo','python3','startup.py'])
