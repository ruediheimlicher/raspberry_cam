#!/usr/bin/env python3
import subprocess
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
print ("camera_full")

# Anzeige Camera ON setzen
GPIO.setup(10,GPIO.OUT)
GPIO.output(10,1)

#Anzeige Camera ON setzen bei Monitor
GPIO.setup(22,GPIO.OUT)
GPIO.output(22,1)

subprocess.call(['raspivid','--preview','-80,0,800,480','-t','0','-fps','30','-roi','0,0.125,0.99,0.85'])
