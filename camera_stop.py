#!/usr/bin/env python
import subprocess
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#GPIO.VERSION
#print ('Version: ',GPIO.VERSION)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,1)

subprocess.call(['pkill','raspivid'])
