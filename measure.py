import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

#Pin setup
#pin_V = ?
pin_clock = 16
pin_data = 18

#Variables
clock = 1
lastClock = 1
time = 0
timeStart = 0
out = 0

GPIO.setup(pin_clock, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_data, GPIO.IN, pull_up_down=GPIO.PUD_UP)

lastClock = clock
clock = GPIO.digitalRead(clockIn)

try:
	while True:
    	#GPIO.input(pin_data) reference the pin
		if lastClock ==1 and clock ==0:
			out = GPIO.digitalRead(dataIn)+GPIO.digitalRead(dataIn)+GPIO.digitalRead(dataIn) #Triple sample remove glitches
		if (micros() - time) > 800:
			Serial.printIn(" ")
		elif (micros() - time) > 400:
			print(" ")
		if (out > 1):
			print("1")
		else:
			print("0")
		time = micros()

except KeyboardInterrupt:
	GPIO.cleanup()
print("Exiting")
