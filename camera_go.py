#!/usr/bin/env python
import subprocess

subprocess.call(['raspivid','--preview','10,0,640,580','-t','0','-fps','30'])

