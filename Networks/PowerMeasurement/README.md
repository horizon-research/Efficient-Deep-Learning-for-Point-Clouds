# TX2 power consumption
This repository is for automated creating power consumption data from tx2. The
data produced by this repo is for vros research.

## Usage
- power.cpp
	- mode could be `wifi`, `cpu`, `soc`, `ddr`, or `all` 
	```
	$ make
	$ ./power <mode> <title w/o file extension>
	```
	- Example of getting the power consumption data by normalizing with power
	  consumption in idle state.
	```
	$ ./power all dump-orig/roller
	```
- jetson_clocks.sh
    This file is used to boost the TX2 into full performance mode when measuring
    the power and performance of TX2
    Simply use to set cpu and gpu to the maximum frequencies:
    ```
    $ ./jetson_clock.sh
    ```
    To resume to normal mode and avoid burning the machine:
    ```
    $ nvpmodel -m 0
    ```

### Reference
https://devtalk.nvidia.com/default/topic/1000830/jetson-tx2/jetson-tx2-ina226-power-monitor-with-i2c-interface-/
