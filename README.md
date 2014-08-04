serial-driller
==============

Provides list of device serial numbers across a fleet of Junos devices

### Usage

Script assumes a common username/password across devices.  Pass a text file containing device IPs (one per line), and the script will return IP to serial-number mappings in .csv format.  Devices such SRX chassis clusters, EX Virtual Chassis etc will return comma-separated list of all device serial numbers.

```
serial-driller devices.txt

Serial-Driller 
. - success
x - error

Reading device list:      ...x..........
Gathering serial numbers: ...x..x.......

10.0.1.1,SRX220H,AG73738287162
10.0.1.2,SRX220H,AG29393887177
10.0.1.3,SRX220H,AG29918827717
10.0.14,IP Address error
10.0.1.5,SRX220H,AG29918827727
10.0.1.6,SRX100B,AG29918827738
10.0.1.7,Device Unreachable
10.0.1.8,SRX220H,AG82773771771
10.0.1.9,SRX220H,AG82773771772
10.0.1.10,SRX220H,AG82773771773
10.0.1.11,SRX240H,AG82838281781,AG82838281781
10.0.1.12,SRX100B,AG82773771775
10.0.1.13,SRX100B,AG82773771776
10.0.1.14,EX4200-VC,AG82773771777,AG82773771778,AG82773771779,AG82773771710,AG82773771711
```
