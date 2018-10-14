import pycom
import time
import sys, os

pycom.heartbeat(False)

try:
    while True:
        pycom.rgbled(0xFF0000)  # Red
        print("ROJO")
        time.sleep(1)
        pycom.rgbled(0x00FF00)  # Green
        print("VERDE")
        time.sleep(1)
        pycom.rgbled(0x0000FF)  # Blue
        print("AZUL")
        time.sleep(1)

except KeyboardInterrupt:
        print('Interrupted')
        try:
            pycom.heartbeat(True)
            sys.exit(0)
        except SystemExit:
            print("SystemExit")

#sys.exit(0)
