import string
import os
import sys
import time

# pip install evdev
from evdev import InputDevice
from select import select

# look for a /dev/input/by-id/usb...kbd or something similar
DEVICE = "/dev/input/by-id/usb-413c_2003-event-kbd"

dev = InputDevice(DEVICE)

while True:

    # wait for keypad command
    r, w, x = select([dev], [], [])

    # read keypad        
    for event in dev.read():
        if event.type==1 and event.value==1:
            if event.code in keys:
                print "KEY CODE: " + event.code
                # do something with this key press
                # ...
