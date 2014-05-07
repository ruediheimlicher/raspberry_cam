#!/bin/bash

# Wird in rc.local beim Start aufgerufen.
# GPIO23 setzen(ist PORT 16)
echo "23" > /sys/class/gpio/export
chmod 777 -R /sys/class/gpio/gpio23
echo "in" > /sys/class/gpio/gpio23/direction

# GPIO18 setzen(ist Port 12)
echo "18" > /sys/class/gpio/export
chmod 777 -R /sys/class/gpio/gpio18
echo "out" > /sys/class/gpio/gpio18/direction
echo "1" > /sys/class/gpio/gpio18/value

sudo python3 ./home/pi/Desktop/Camera/startup_int.py &
sudo python3 ./home/pi/Desktop/Camera/camera_full.py
#sudo python3 ./home/pi/Desktop/Camera/startup.py
#sudo python3 ./home/pi/Desktop/Camera/camera_full.py
