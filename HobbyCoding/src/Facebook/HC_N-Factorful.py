'''
Created on Jan 29, 2011

@author: ashwin

 Licensed to Ashwin Panchapakesan under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 Ashwin licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
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