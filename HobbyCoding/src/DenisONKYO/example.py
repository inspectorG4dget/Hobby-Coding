from sys import path as syspath
from os import getcwd as pwd
from time import sleep

syspath.append(pwd())

import DenisONKYO


print 'starting'

# Create a receiver object attached to the host 192.168.1.124
receiver = DenisONKYO.eISCP('192.168.10.148')

# Turn the receiver off
#receiver.writeCommandFromName('Power OFF')

# Turn the receiver on
#receiver.writeCommandFromName('Power ON')

# Select the PC input
#receiver.writeCommandFromName('Computer/PC')

print 'sleeping 7 seconds. Select a song'
#sleep(7)

# Increasing volume
print 'increasing volume'
#for _ in xrange(10):
#		receiver.writeCommandFromName('Volume Up')
#		sleep(0.5)

# Decreasing volume
print 'decreasing volume'
for _ in xrange(10): 
	receiver.writeCommandFromName('Volume Down')
#	sleep(0.5)

# Done watching a movie, shut it off.
#receiver.writeCommandFromName('Power OFF')

print 'done'
