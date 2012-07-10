'''
Created on Jan 18, 2011

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

def fit(L,k):
	""" Return i such that:
		1. 0 <= i <= len(L)
		2. sum(L[:i]) <= k"""
	total = 0
	i = 0
	l = len(L)
	while total <= k and i<l:
		total += L[i]
		i += 1
	return i
		
def calc(R, k, L):
	total = 0
	for _ in range(R):
		i = fit(L, k)
		total += sum(L[:i])
		l = len(L)
		L[:l-i], L[l-i:] = L[i:], L[:i]
	return total

def run(infilepath, outfilepath):
	output = open(outfilepath, 'w')
	with open(infilepath, 'r') as input:
		T = int(input.readline().strip())
		for t in range(T):
			print t
			line1 = input.readline().strip()
			line2 = input.readline().strip()

			R, k, N = [int(i) for i in line1.strip().split()]			
			L = [int(i) for i in line2.strip().split()]
			
			output.write("Case #%d: %d\n" %(t+1, calc(R, k, L)))
			
		output.close()
	
if __name__ == "__main__":
	import timeit
	print 'starting'
	
	infilepath = "C-small-practice.in"
	outfilepath = "C-small-practice.out"
	t = timeit.Timer("run(infilepath, outfilepath)", "from __main__ import run, infilepath, outfilepath")
	print t.timeit(1)
#	run(infilepath, outfilepath)
	
	print 'done'