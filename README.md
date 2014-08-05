serial-driller
==============

Provides a hardware inventory across a fleet of Junos devices

### Requirements

- Junos PyEZ installed
- Common username and password/SSH key across devices.  
- Netconf over SSH is enabled on all devices:

```
set system services netconf ssh
```

### Usage

Pass a text file containing device IPs (one per line), and the script will return IP to serial-number and hardare model mappings in .csv format.  

```
serial-driller devices.txt

<<<<<<< HEAD
Serial-Driller

Username: bdale
Password (leave blank to use SSH Keys): 
=======
Serial-Driller 
Username: operator
Password:

>>>>>>> FETCH_HEAD
. - success
x - error
Reading device list: .No handlers could be found for logger "paramiko.hostkeys"
....x
172.16.10.254,AD2409AA0254,SRX210H
172.16.10.253,GR0211538683,EX2200-C-12P-2G, POE+
10.0.254.10,AT3209AF0139,SRX100B
10.0.255.6,GR0211480357,EX2200-C-12P-2G, POE+
10.0.255.4,AT3209AF0139,SRX100B
abc,IP Address Error,N/A
```

### TODO:

Test against devices such SRX chassis clusters, EX Virtual Chassis etc and return unique device entries of all member devices
