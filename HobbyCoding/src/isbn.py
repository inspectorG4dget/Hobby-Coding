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

def valid10(isbn):
	"""Return True iff the input string is a valid ISBN-10"""
	sum = 0
	for i in range(0, 10):
		weight = 10 - i
		digit = int(isbn[i])
		sum += digit*weight
		
	return not sum%11
	
def generateIsbn10(n):
	"""Generate all valid ISBN-10 < n"""
	curr = 0
	for _ in range(n):
		done = False
		while not done:
			prospect = "%010d" %curr
			if valid10(prospect):
				done = True
				yield prospect
			curr += 1