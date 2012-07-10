'''
Created on Jan 7, 2011

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
import math

def resolve(n):
	""" This function takes an int as input and returns a set of tuples.
		If the int is expressible as the sum of two squares, the set contains sorted 2-int-tuples.
		The sum of the squares of the ints in each tuple will add up to n"""
		
	answer = set([])
	
	for i in range(int(math.sqrt(n)) +1):
		s1 = i**2
		s2 = n-s1
		if not (math.sqrt(s2) %1):
			a = [s1, s2]
			a.sort()
			answer.add(tuple(a))
			
	return answer

def run(infilepath, outfilepath):
	fin = open(infilepath, 'r')
	fout = open(outfilepath, 'w')
	
	N = int(fin.readline().strip())
	for _ in range(N):
		n = int(fin.readline().strip())
		fout.write("%d\n" %len(resolve(n)))
		
	fin.close()
	fout.close()
	
if __name__ == "__main__":
	print 'starting'
	infilepath = "testin.txt"
	outfilepath = "testout.txt"
	run(infilepath, outfilepath)
	print 'done'