

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
try:
	GPIO.output(37, GPIO.HIGH)
	print('Blink')
	time.sleep(1)
	GPIO.output(37, GPIO.LOW)
except:
	print('Error')
