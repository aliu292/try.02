#!/usr/bin/env python

import time
from time import sleep
import os
import RPi.GPIO as GPIO
import sys
import subprocess
from subprocess import Popen
from subprocess import PIPE

import serial
import shlex

def sensorCallback(channel):
  # Called if sensor output changes
  if GPIO.input(channel):
    # No magnet
    print("HIGH")
  else:
    # Magnet
    print("LOW")

#definition du serial
#ser = serial.Serial('/dev/ttyACMaa, 9600)

#killomx = "sudo killall -s 9 omxplayer.bin"
#os.system(killomx)
player = subprocess.Popen(["omxplayer"])

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(18, GPIO.IN)

hallpin = 18
sleepTime = 0.1
pausestat = 0
playstate = 0

GPIO.setup( hallpin, GPIO.IN)

movie1 = ("/home/pi/Desktop/movie1.mp4")

#try:
while True:
    #omxc=subprocess.Popen(['omxplayer', '-b', movie1])

    if (GPIO.input(hallpin) == False):
    #print("magnet detected")
        omxprocess = subprocess.Popen(['omxplayer', movie1], stdin=subprocess.PIPE,stdout = None, bufsize = 0)
        time.sleep(5)
        omxprocess.stdin.write(b' ')

    if (GPIO.input(hallpin) == True):
        sleep(1)
        if (GPIO.input(hallpin) == True):
            print ("Stop")
            #player.stdin.write("p")
            os.system('killall omxplayer.bin')
    #print("magnet not detected")
    #os.system('killall omxplayer.bin')
        #os.system('/home/pi/mu_code/dbuscontrol.sh pause')
        #omxc=subprocess.Popen(['omxplayer', '-i', movie1])
#sleep(sleepTime)

#except KeyboardInterrupt:
    #Reset GPIO settings
    #os.system('killall omxplayer.bin')
    #GPIO.cleanup()
#except KeyboardInterrupt:
	#print ("Exception: KeyboardInterrupt")