#!/usr/bin/python

import wiringpi
import time
import sys

wiringpi.wiringPiSetup()
#wiringpi.pinMode(1, wiringpi.PWM_OUTPUT)

#for x in xrange(0,1024):
#    print x
#    wiringpi.pwmWrite(1,x)
#    time.sleep(0.005)

#for x in xrange(1024,0,-1):
#    print x
#    wiringpi.pwmWrite(1,x)
#    time.sleep(0.005)

wiringpi.softPwmCreate(8, 0, 100)

for x in xrange(0,100):
    wiringpi.softPwmWrite(8,x)
    time.sleep(0.01)

for x in xrange(100,0,-1):
    wiringpi.softPwmWrite(8,x)
    time.sleep(0.01)

wiringpi.softPwmWrite(8,int(sys.argv[1]))
