#LED Pinout test
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

pins = [17, 18, 27, 22]

#i is the index of the array, pin is the value, e.g. 0,17
for i, pin in enumerate(pins):
	GPIO.setup(pin, GPIO.OUT)
	for j in range(i+1):
		GPIO.output(pin,1)
		time.sleep(0.5)
		GPIO.output(pin,0)
		time.sleep(0.5)
GPIO.cleanup()

