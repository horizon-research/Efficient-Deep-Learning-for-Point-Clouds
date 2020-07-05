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
## How to measure the power of execution time
	
To recreate some of measurements in our paper, you can create two windows from your terminals. One is used to launch
the network. While the network model is launched, use the second windows to measure the power consumption on TX2. For
example:
```
$ ./power gpu [NETWORK_NAME]
```
Then, Kill the `power` program while the network model is still running. The measured GPU power number will be stored in
a file named `[NETWORK_NAME]_gpu.txt`. Average the number stored in the file, you will get the average power consumption 
for one particular network.

### Reference
https://devtalk.nvidia.com/default/topic/1000830/jetson-tx2/jetson-tx2-ina226-power-monitor-with-i2c-interface-/
