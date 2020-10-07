# Demo

LGTC is communicating with Vesna over serial connection with ALH protocol.

## Run experiment localy

### ALH setup

To run the experiment locally on the machine (when you are connected to the LGTC via ssh for example), you must first run the script /deployment/tasks/run-lora-load which will start the ALH protocol on the Vesna device. Then you can execute the local scripts to start the application.

### How to use it

There are 6 handlers implemented for LGTC to communicate with Vesna over ALH protocol:

* hello - returns "HelloWorld" and arguments that have been sent.
* loraRadioInfo - in case that everything is OK, Vesna will return "SX1272 radio connected".
* loraRxStart - set the radio in receiving mode. Here we have to set up 4 parameters:
    * Frequency in Hz (860 MHz ~ 920 MHz)
    * Bandwidth (125, 250 or 500 kHz)
    * Spreading factor (7 ~ 12)
    * Coding rate (CR4_5, CR4_6, CR4_7 or CR4_8)
    * A usage example: *```get loraRxStart?frequency=868500000&bw=125&sf=7&cr=4_5```*
* loraRxRead - we send *```get loraRxRead```* when we want to read received message
* loraTxStart - besides the same parameters as at the receiving command, we also have to add:
    * Power in dBm (2 dBm ~ 14 dBm)
    * Message (up to 64 Bytes)
* loraTxDone - if we want to make sure that packet was sent, we can send *```get loraTxDone```*

## Run experiment remotely

We can control the Vesna device also remotely with ALH protocol. Again, Vesna must firstly set up ALH server (/deployment/tasks/run-lora-load). Then you can connect to it and send the handlers to control the LoRa radio.