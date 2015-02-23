#!/usr/bin/python

import time
import subprocess
from RPi import GPIO 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

while True:
  input_value = GPIO.input(11)
  if input_value == False:
    print("The Button has been pressed.")
    subprocess.check_call(r"""/home/pi/bin/bw_lcd -T 0,0 "`date '+%a %d %r'` " """, shell=True)
    subprocess.check_call(r"""/home/pi/bin/bw_lcd -T 0,1 " `hostname -I`" """, shell=True)
    while input_value == False:
      input_value = GPIO.input(11)
      time.sleep(0.01)
  else:
    print("The Button has been released.")
    subprocess.check_call(r"""/home/pi/bin/bw_lcd -C  """, shell=True)
    while input_value == True:
      input_value = GPIO.input(11)
      time.sleep(0.01)
