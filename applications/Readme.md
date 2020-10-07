# Description

## Local test

To test them locally, run:
> make <app_name>.olimex -j9 \
> python3 serial_monitor.py -o results.txt -p ttyUSB0 -r

## Testbed

To use autonomous testbed deployment, please follow already made templates or stick to the following rules:

* Application folder should have number indicator in front of the app name (XX_)
* The application script must have the same name as the folder name
* If there is a separate script for root node, it should have suffix "-root" at the end of its name. Otherwise root node will be flashed with the same file as normal nodes, just serial_monitor will send root command to it.

For more information on why to do this, check comments in *logatec-experiment/deployment/tasks/run-experiment-root*.
