from network import LoRa
import socket
import time
import pycom
import sys
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915

pycom.heartbeat(False)

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

pycom.rgbled(0xFF0000)  # Red

while True:
    print("====Waiting to receive Ping====")

    if s.recv(64) == b'Ping':
        print("Received ping successfully!!!")
        s.send('Pong')
        pycom.rgbled(0x00FF00)  # Green
        time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(5)
