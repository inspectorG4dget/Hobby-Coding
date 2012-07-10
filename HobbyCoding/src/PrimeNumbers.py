'''
Created on Sep 24, 2010

@@author: ashwin

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

from math import sqrt

def primeNumbers(n):
	""" return a list of prime numbers such that all numbers in the list are at most n
		1 is a prime number"""
	
	answer = []
	if n <= 2:
		answer.append(n)
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

def generate(n):
	""" Yield the first n prime numbers"""

	primes = [2]
	curr = 2
	for _ in range(n-1):
		p = next(curr, primes)
		primes.append(p)
		curr = p
		yield p
		
def next(n, primes=[]):
	""" Return a number p such that 
		1. p is co-prime to every number in primes
		2. p>n and p-n is as small as possible"""
	if primes:
		curr = n+1
		while 1:
			if isPrime(curr, primes):
				return curr
			else:
				curr += 1
	else:
		primes = [2]
		for i in range(3, n+1, 2):
			if isPrime(i, primes):
				primes.append(i)
		curr = n+1
		while not isPrime(curr):
			curr += 1
		return curr
				

def sumOfTwoPrimes(n):
	"""Express n>3 as the sum of two primes or print that it's not possible to do so"""
	
	primes = primeNumbers(n)
	for p in primes:
		if n-p in primes:
			return (p, n-p)
	return ()

def isPrime(n, primes=[]):
	""" Return True iff n is a prime number. 
		If primes is non-empty, return true iff n is co-prime to every number in primes. """
	
	if not len(primes):
		if n <= 2:
			return True
		elif n%2 == 0:
			return False
		else:
#			prime = True
#			for i in range(3, n, 2):
#				if n%i == 0:
#					prime = False
#			if prime:
#				return True
			for i in range(3, int(sqrt(n))+1, 2):
				if not n%i:
					return False
			return True
	else:
		for p in primes:
			if not n%p:
				return False
		return True

if __name__ == "__main__":
	import timeit
#	for i in range(4, 20):
#		doable = sumOfTwoPrimes(i)
#		if doable:
#			print "%d can be represented as the sum of two primes: %d and %d:" %(i, doable[0], doable[1])
#		else:
#			print "%d cannot be represented as the sum of two primes" %i

#	for i in generate(9976): print i
	
#	nums = [2,3,10,32,85,31,104491]
#	for i in nums:
#		print i, ["C","P"][int(isPrime(i))]
#
#	t = timeit.Timer("for i in generate(9976): print i", "from __main__ import generate")
#	print t.timeit(1)
	print next(104491)