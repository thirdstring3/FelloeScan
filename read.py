#!/usr/bin/python

import serial, string

#dialin = "usb-413c_2003-event-kbd"

output = " "
#ser = serial.Serial('/dev/input/by-id/usb-413c_2003-event-kbd', 19200, 8, 'N', 1, timeout=1)
while True:
  print "----"
  while output != "":
	xtest = input('Press ')
	output = xtest 
	#output = ser.readline()
  print output
  output = " "
