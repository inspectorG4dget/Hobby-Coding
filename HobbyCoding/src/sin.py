'''
Created on Sep 25, 2010

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

def validate(sin):
	"""Check if the input string is a valid SIN"""
	check = 121212121
	checksum = 0
	for p in range(10):
		s = (int(sin)%(10 ** p))
		if p:
			s /= 10 ** (p-1)
		
		c = (check%(10 ** p))
		if p:
			c /= 10 ** (p-1)
		
		mult = s*c
		if mult/10:
			mult = mult/10 + mult%10
		
		checksum += mult
		
	return not checksum%10
	
def genSin(n):
	"""Generate the first n many SINs"""
	curr = 100000000
	for _ in range(n):
		done = False
		while not done and curr < 10000000000:
			if validate(curr):
				done = True
				yield curr
			curr += 1

def findSin(lower, upper):
	"""Generate all valid lower <= SINs <= upper. Return False if lower > 10000000000"""
	if lower > 10000000000:
		yield False
	else:
		curr = int(lower)
		done = False
		
		while not done and curr<10000000000 and curr<=upper:
			if validate(curr):
				done = True
				yield curr
			curr += 1
	
if __name__ == "__main__":
	for i in genSin(10):
		print i