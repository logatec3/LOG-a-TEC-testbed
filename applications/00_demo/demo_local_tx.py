import time
import serial
from vesna import alh

freq = 868100000
bw = 125
sf = 12
cr = "4_5"
pwr = 2

ser = serial.Serial("/dev/ttyS2", 115200)
node = alh.ALHTerminal(ser)

print(node.get("loraRadioInfo"))

prm = "frequency=%s&bw=%s&sf=%s&cr=%s&pwr=%s" % (freq, bw, sf, cr, pwr)

for i in range(100):
    res = node.post("loraTxStart", "hello", prm)
    print(res)
    print"-----" + (str(i) + "-----")
    time.sleep(2)

print("Done!")