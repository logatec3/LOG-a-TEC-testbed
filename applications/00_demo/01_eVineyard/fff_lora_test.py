# ------------------------------------------------------------------------
# DESCRIPTION
# ------------------------------------------------------------------------
# Send packet every second
# Every 2 hours increase power of transmission by factor of 2 (2~14dBm)
# Experiment will last for 14 hours
# ------------------------------------------------------------------------

import time
import serial
from vesna import alh

freq = 868100000    # Frequency
bw = 125            # Bandwidth
sf = 12             # Spreading factor
cr = "4_5"          # CR
pwr = 2             # Power

ser = serial.Serial("/dev/ttyS2", 115200)
node = alh.ALHTerminal(ser)

print(node.get("loraRadioInfo"))

prm = "frequency=%s&bw=%s&sf=%s&cr=%s&pwr=%s" % (freq, bw, sf, cr, pwr)

for j in range(7):
    pwr = 2 * j
    prm = "frequency=%s&bw=%s&sf=%s&cr=%s&pwr=%s" % (freq, bw, sf, cr, pwr)

    # Transmit message "hello123" for 7200 seconds
    for i in range(7200):
        res = node.post("loraTxStart", "hello113", prm)
        print(res)
        print"-----" + (str(i) + "-----")
        time.sleep(1)

print("Done!")
