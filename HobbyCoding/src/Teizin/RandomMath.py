'''
Created on Jul 17, 2011

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

from random import randint, choice as choose

def ask(msg):
	return raw_input("%s: " %msg)

def getNumbers(n, L, U):
	return [randint(L, U) for _ in xrange(n)]

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x/y

if __name__ == "__main__":
	
	func = {'-':subtract, "+":add, '/':divide, "*":multiply}
	# controls the digit-limit for +/- questions. If you want 7-digit numbers, ask for 10**8 -1. 10**7 -1 for 6-digit numbers
	addlimit = 10**8 -1
	
	# controls the digit-limit for +/- questions. If you want 3-digit numbers, ask for 10**4 -1. 10**3 -1 for 2-digit numbers
	divlimit = 10**4 -1
	
	while 1:
		op = choose("-+")
		if op in '+-':	# change '+-' to '-/*+' to include multiplication and division problems
			nums = nums = ["%07d" %s for s in getNumbers(2, 0, addlimit)]
		else:
			nums = ["%04d" %s for s in getNumbers(2, 0, divlimit)]
			
		gotResp = False
		while not gotResp:
			try:
				response = int(ask("what is \n%s %s \n%s" %(nums[0], op, nums[1])))
				gotResp = True
			except ValueError:
				'Oops, typo. Try again'
		
		if response != func[op](*[int(n) for n in nums]):
			print 'you fail'
		else:
			print 'woo hoo! next'