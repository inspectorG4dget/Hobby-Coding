'''
Created on Jan 29, 2011

@author: ashwin
'''

def primeNumbers(n):
	""" return a list of prime numbers such that all numbers in the list are at most n
		1 is not a prime number"""
	
	answer = [2]
	if n <= 2:
		return answer
	else:
		for i in range(3, n+1, 2):
			prime = True
			for p in answer:
				if i%p == 0:
					prime = False
					break
			if prime:
				answer.append(i)
				
	return answer

def nfactorful(N, primes, n):
	""" Given N and a list of primes where each prime is at most n/2, return True iff there are n primes that evenly divides N"""
	
	count = 0
	for p in primes:
		if not N%p: count += 1
		
	return count == n

def run(infilepath, outfilepath):
	input = open(infilepath, 'r')
	output = open(outfilepath, 'w')
	
	N = int(input.readline().strip())
	
	for _ in range(N):
		a, b, n = [int(i) for i in input.readline().strip().split()]
		print _
		
		count = 0
		for i in range(a, b+1):
			if nfactorful(i, [p for p in primeNumbers(i)], n):
				count += 1
		output.write("%d\n" %count)
	input.close()
	output.close()
		
if __name__ == "__main__":
	print 'starting'
	
	infilepath = 'testin.txt'
	outfilepath = 'testout.txt'
	
	run(infilepath, outfilepath)
	
	print 'done'