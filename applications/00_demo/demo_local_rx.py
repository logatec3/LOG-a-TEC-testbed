import time
import serial
from vesna import alh

freq = 868100000
bw = 125
sf = 12
cr = "4_5"

ser = serial.Serial("/dev/ttyS2", 115200)
node = alh.ALHTerminal(ser)

print(node.get("loraRadioInfo"))

prm = "frequency=%s&bw=%s&sf=%s&cr=%s" % (freq, bw, sf, cr)

res = node.get("loraRxStart", prm)

print(res)

for i in range(600):
        res = node.get("loraRxRead")
        if str(res).strip() != "No packet received":
                print("Received")
                print(str(res).strip())
                # Restart to receiver mode
                node.get("loraRxStart", prm)
        else:
                print("No packet")
        time.sleep(1)

print("Done!")
