#!/usr/bin/env python
import subprocess

#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
#subprocess.call(['raspivid','--fullscreen','-t','0','-fps','30'])
subprocess.call(['raspivid','--preview','-80,0,800,480','-t','0','-fps','30','--rotation','180','-roi','0,0.125,0.99,0.85'])
