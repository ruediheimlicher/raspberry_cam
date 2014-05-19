#!/usr/bin/env python
import subprocess
import RPi.GPIO as GPIO
import time as TIME

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#GPIO.VERSION
#print ('Version: ',GPIO.VERSION)
GPIO.setup(10,GPIO.OUT)
GPIO.output(10,0)
TIME.sleep(5)
GPIO.output(10,1)
TIME.sleep(5)
GPIO.output(10,0)
TIME.sleep(5)
subprocess.call(['pkill','raspivid'])
