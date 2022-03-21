# transmitter interface 145320 @ xb8

import machine
from time import sleep
import math
import network
from esp import espnow
from struct import pack

ON = 0
OFF = 1

pin = 2
beep_pin = 0
switch = machine.Pin(pin, machine.Pin.IN)
beep = machine.Pin(beep_pin, machine.Pin.OUT)
beep.value(OFF)

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)
now = espnow.ESPNow()
now.init()

print("Starting transmitter...")
print("".join("%02x:" % i for i in w0.config('mac'))[0:-1])

# c4:5b:be:62:ad:5d
# b'\xc4[\xbeb\xad'
peer = b'\xc4[\xbeb\xad]'
now.add_peer(peer)

while True:
    if switch.value() == ON:
        print("SWITCH PRESSED")
        now.send(peer, 'hello', True)
        beep.value(ON)
        sleep(.15)
        beep.value(OFF)
    sleep(0.25)
