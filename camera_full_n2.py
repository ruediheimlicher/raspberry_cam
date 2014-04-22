#!/usr/bin/python3
import subprocess

if subprocess.call(['pidof','raspivid']):
	print "raspivid not running"
	subprocess.call(['raspivid','--preview','-80,0,800,480','-t','0','-fps','30','-roi','0,0.125,0.99,0.85'])
else:
	print "raspivid running"	
	subprocess.call(['pkill','raspivid'])
		

