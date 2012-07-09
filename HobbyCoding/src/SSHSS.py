'''
Created on Nov 18, 2010

@author: ashwin
'''

from AlienNumber import decToAlien
import random

def bin(n):
	return decToAlien(n, '01')

def isSS(L):
	t = L[-1]
	X = L[:-1]
	for i in range(2**len(X)):
		b = bin(i)
		select = '0'*(len(X)-(len(b))) + bin(i)
		s = []
			
		for c in range(len(select)):
			if int(select[c]):
				s.append(X[c])
		if sum(s) == t:
			print s
			return True
	return False
			
def isHSS(L):
	l = 2**len(L)
	for i in range(l):
		b = bin(i)
		select = '0'*(len(L)-(len(b))) + b
		s1, s2 = [], []
		for c in range(len(select)):
			if int(select[c]):
				s1.append(L[c])
			else:
				s2.append(L[c])
		if sum(s1) == sum(s2):
			print "s1:", s1, "s2:", s2
			return True
	return False
	
def test(L):
	ss = isSS(L)
	y = abs(sum(L[:-1]) - (2* L[-1]))
#	print "y: %d" %y
	hss = isHSS(L[:-1]+[y])
	if ss == hss:
#		print ss, hss
		return True
	else:
		return False


if __name__ == "__main__":
	print "Starting"
	for i in range(3, 20):
		for _ in range(100):
			L=[random.randint(1,1000) for _ in range(i)]
			print L
			if not test(L):
				print "test fails on:", L
	print "Done"