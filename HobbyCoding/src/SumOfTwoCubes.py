'''
Created on Sep 17, 2010

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

def resolve(n):
	"""The input n is an integer. This function will returns a tuple. 
		If n is expressible as the sum of two cubes, the returned tuple will contain the two integers, 
		the sum of whose cubes is n. If no two such integers exist, then an empty tuple is returned"""
		
	for i in range(n):
		j = -1
		sum = i**3
		while sum < n:
			j += 1
			sum = (i**3) + (j**3)

		if sum == n:
			return (i, j)
	return ()

def run(n):
	answer = resolve(n)
	if answer:
		print "%d can be expressed as the sum of the cubes of %d and %d" %(n, answer[0], answer[1])
	else:
		print "%d cannot be expressed as the sum of two cubes" %n
		
if __name__ == "__main__":
	while True:
		try:
			input = int(raw_input("Enter a number: "))
			run(input)
		except ValueError:
			print "Your input was not a number. Try again."