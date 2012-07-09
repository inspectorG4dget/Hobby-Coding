'''
Created on Sep 25, 2010

@author: ashwin
'''

from random import randint as rand

mac = [ 0x00, 0x16, 0x3e, \
	rand(0x00, 0x7f), \
	rand(0x00, 0x7f), \
	rand(0x00, 0x7f) ]

print ":".join(map(lambda x: "%02x" % x, mac))