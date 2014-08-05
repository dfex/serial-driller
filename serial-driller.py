#!/usr/bin/env python

## serial-driller.py - 04/08/2014
## ben.dale@gmail.com
## Automated Junos device information retrieval
## 

import sys
import re
from getpass import getpass
from pprint import pprint
from jnpr.junos import Device

sys.stdout.write("Serial-Driller\n\n")
if len(sys.argv) != 2:
	sys.stdout.write("Error: Missing parameter\n")
	sys.stdout.write("Usage: serial-driller <hostlist.csv>\n")
	sys.exit()
	
username = raw_input('Username: ')
password = getpass('Password (leave blank to use SSH Key): ')
sys.stdout.write(". - success\n")
sys.stdout.write("x - error\n")

deviceInventory = []

# Regex for routable IP addresses (1.0.0.0-223.255.255.255)
inetRegex = re.compile("^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-1][0-9]|22[0-3])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$") 


sys.stdout.write("Reading device list: ")
sys.stdout.flush()
hostsfile = open(str(sys.argv[1]),'r')
for hostAddress in hostsfile:
	if inetRegex.match(str(hostAddress)):
		sys.stdout.write('.')
		sys.stdout.flush()
		if password != '':
			dev = Device(host=hostAddress.rstrip('\n'),user=username,passwd=password)
		else:
			dev = Device(host=hostAddress.rstrip('\n'),user=username)
		dev.open()		
		deviceInventory.append({"IP Address":str(hostAddress).rstrip('\n'),"Serial Number":dev.facts['serialnumber'],"Model":dev.facts['model']})
		dev.close()
	else:	
		sys.stdout.write("x")
		sys.stdout.flush()
		deviceInventory.append({"IP Address":str(hostAddress).rstrip('\n'),"Serial Number":"IP Address Error","Model":"N/A"})

sys.stdout.write('\n')
for device in deviceInventory:
	line = device["IP Address"] + ',' + device["Serial Number"] + ',' + device ["Model"] + '\n'
	sys.stdout.write(line)
	sys.stdout.flush()