import sys

fp = open('/dev/input/by-id/usb-413c_2003-event-kbd', 'rb')

while True:
	buffer = fp.read(8)
	for c in buffer:
		if ord(c) > 0:
			print ord(c)
	print "\n"
