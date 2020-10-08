# Demo

ALH protocol is used to control Vesna device, which has LoRa radio connected to it. We can communicate with it locally - LGTC is communicating with Vesna over serial connection with ALH, or we can do it remotely - our device can communicate with Vesna over www.
More info about ALH protocol can be found on [link](http://log-a-tec.eu/cr-software.html#testbed-access-using-alh-protocol "Testbed access using ALH protocol").

## Run experiment locally

To run the experiment locally on the machine (when you are connected to the LGTC via ssh for example), you must first run the script /deployment/tasks/run-lora-load which will start the ALH protocol on the Vesna device. Then you can execute the local scripts - check the scripts *demo_local-tx.py* and *demo_local_rx.py*.

## Run experiment remotely

Again, Vesna must firstly set up ALH server (/deployment/tasks/run-lora-load). Then you can connect to it and send the GET and POST handlers to control the LoRa radio. Check the script *demo_remote.py*.

## How to use it

There are 6 handlers implemented for LGTC to communicate with Vesna:

* **hello** - returns "HelloWorld" and arguments that have been sent.
* **loraRadioInfo** - in case that everything is OK, Vesna will return "SX1272 radio connected".
* **loraRxStart** - set the radio in receiving mode. Here we have to set up 4 parameters:
    * Frequency in Hz (860 MHz ~ 920 MHz)
    * Bandwidth (125, 250 or 500 kHz)
    * Spreading factor (7 ~ 12)¸
    * Coding rate (CR4_5, CR4_6, CR4_7 or CR4_8)
    * A usage example: *```get loraRxStart?frequency=868500000&bw=125&sf=7&cr=4_5```*
* **loraRxRead** - we send *```get loraRxRead```* when we want to read received message
* **loraTxStart** - besides the same parameters as at the RxStart command, we also have to add:
    * Power in dBm (2 dBm ~ 14 dBm)
    * Message to be send (up to 64 Bytes)
* **loraTxDone** - will tell us if the packet was sent successfully.
0,
