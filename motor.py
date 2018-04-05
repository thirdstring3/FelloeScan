# 1 = GPIO.HIGH = True
# 0 = GPIO.LOW = False

import time
import math
import RPi.GPIO as GPIO
print(GPIO.RPI_INFO)
GPIO.setmode(GPIO.BOARD) #Using 26/40 board pin layout to eliminate confusion

#Setup Variables, will be replaced by array data or csv file later
#wiringPi pins do not match Board Pins (nor BCM GPIO pins)
m_responseDelay = 4
m_stepsPerRevolution = 3200
m_stepDelay = 10
m_stepPin = 7 #wiringPi 7
m_directionPin = 12 #wiringPi 1
m_stabilityDelay = 1
m_enablePin = 11 #wiringPi 0

def usleep(microseconds):
	#if usleep(microseconds) != 0:
	#	print("Error sleeping thread, errno="+errno)
	time.sleep(microseconds/1000000)
	print(microseconds)
	return

def initialize():
	#Disable stepper
	#pinMode(enablePin, OUTPUT);
	GPIO.setup(m_enablePin, GPIO.OUT, initial = 1)
	#digitalWrite (enablePin, HIGH);
	GPIO.output(m_enablePin, False)

	#Put in known state
	#pinMode(stepPin, OUTPUT)
	GPIO.setup(m_stepPin, GPIO.OUT, initial = 0)
	#digitalWrite(stepPin, LOW)
	GPIO.output(m_stepPin, False)

	#pinMode(directionPin, OUTPUT)
	GPIO.setup(m_directionPin, GPIO.OUT, initial = 0)
	#digitalWrite(directionPin, LOW)
	GPIO.output(m_directionPin, False)
	#usleep(responseDelay)
	usleep(m_responseDelay)
	return

def step():
	#digitalWrite(m_stepPin, LOW);
	GPIO.output(m_stepPin, False)
	#usleep(m_responseDelay);
	usleep(m_responseDelay)
	#digitalWrite(m_stepPin, HIGH);
	GPIO.output(m_stepPin, True)
	#usleep(m_responseDelay);
	usleep(m_responseDelay)
	#usleep(m_stepDelay);
	usleep(m_stepDelay)
	return

def rotate(theta):
	#Get the % of a full revolution that theta is and convert to # of steps
	#int numSteps=(theta/(2*PI))*m_stepsPerRevolution;
	#numSteps = int((theta / (2 * math.pi)) * m_stepsPerRevolution)
	#Step the required # of steps
	numSteps = m_stepsPerRevolution
	for i in range(0,numSteps):
		step()

	#Sleep the stability delay amount
	#usleep (m_stabilityDelay);
	usleep(m_stabilityDelay)

	return numSteps

initialize()
rotate(120)

GPIO.cleanup()
