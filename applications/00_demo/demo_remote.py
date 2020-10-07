import os
import unittest
import requests
from vesna import alh
from time import sleep

class LoraTests(unittest.TestCase):
    def setUp(self):
        port = 9000

        rx_ip = os.environ.get("LORA_RX", "127.0.0.1")
        tx_ip = os.environ.get("LORA_TX", "127.0.0.1")
        self.dev = os.environ.get("VESNA_DEV", "/dev/ttyUSB0")

        self.lora_rx = "http://%s:%s" % (rx_ip, port)
        self.lora_tx = "http://%s:%s" % (tx_ip, port)
        self.lora_rx_api = self.lora_rx + "/communicator"
        self.lora_tx_api = self.lora_tx + "/communicator"

        for x in range(100):
            try:
                requests.get(self.lora_rx)
                requests.get(self.lora_tx)
                break
            except:
                sleep(5)

    def test_lora_network(self):
        freq = 868100000
        bw = 125
        sf = 12
        cr = "4_5"
        pwr = 2
        test_msg = "hello lora network"

        node_rx = alh.ALHWeb(self.lora_rx_api, self.dev)
        node_tx = alh.ALHWeb(self.lora_tx_api, self.dev)

        print(node_rx.get("loraRadioInfo").text)
        print(node_tx.get("loraRadioInfo").text)

        prm = "frequency=%s&bw=%s&sf=%s&cr=%s" % (freq, bw, sf, cr)
        res = node_rx.get("loraRxStart", prm)
        print(res.text)

        prm = "frequency=%s&bw=%s&sf=%s&cr=%s&pwr=%s" % (freq, bw, sf, cr, pwr)
        res = node_tx.post("loraTxStart", test_msg, prm)
        print(res.text)

        for i in range(10):
            res = node_rx.get("loraRxRead")

            if "No packet received" not in res.text:
                break

            sleep(1)

        print(res.text)

        self.assertTrue(test_msg in res.text)

if __name__ == '__main__':
    unittest.main()