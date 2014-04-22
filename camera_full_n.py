#!/usr/bin/env python3
import subprocess

#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
#if subprocess.call(['pgrep','raspivid','>','/dev/null']):
print "run?",subprocess.check_output(['pgrep','-c','raspivid'])
#print "raspivid running",subprocess.call(['pgrep','raspivid']>10)
while subprocess.check_output(['pgrep','-c','raspivid']):
	if 1:
		print "raspivid running"
		subprocess.call(['pkill','raspivid'])
		break
		
	subprocess.call(['raspivid','--preview','-80,0,800,480','-t','0','-fps','30','-roi','0,0.125,0.99,0.85'])	
print "exit"
#subprocess.call(['raspivid','--preview','-80,0,800,480','-t','0','-fps','30','-roi','0,0.125,0.99,0.85'])


