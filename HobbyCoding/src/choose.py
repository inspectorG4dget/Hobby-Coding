'''
Created on Dec 9, 2010

@author: ashwin
'''

def fact(n):
	if not n:
		return 1
	else:
		return n*(fact(n-1))
	
def choose(n, k):
	return fact(n)/(fact(k) * fact(n-k))

def run(input):
	n, k = [int(i.strip()) for i in input.split(',')]
	return choose(n, k)

if __name__ == "__main__":
	import sys
	print run(sys.stdin.readline().strip())