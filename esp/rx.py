# Receiver interface @ xec

import network
from esp import espnow
import time
import math
import machine
import neopixel

ON = 0
OFF = 1

neopixel_pin = 2 # D4
np = neopixel.NeoPixel(machine.Pin(neopixel_pin),7)

# Output Pin
output_pin = 0 # D3
out = machine.Pin(output_pin, machine.Pin.OUT)
out.value(OFF)

# A WLAN interface must be active to send()/recv()
w0 = network.WLAN(network.STA_IF)
w0.active(True)
e = espnow.ESPNow()
e.init()

print("Starting receiver...")
print("".join("%02x:" % i for i in w0.config('mac'))[0:-1])
peer = b'\xc4[\xbeb\xba\xdb'
e.add_peer(peer)

np.fill((0,0,0))
np.write()

while True:
    host, msg = e.irecv()
    if msg:
        out.value(ON)
        print(msg.decode('utf-8'))
        np.fill((10,10,10))
        np.write()
        time.sleep(0.5)
        out.value(OFF)
        np.fill((0,0,0))
        np.write()

