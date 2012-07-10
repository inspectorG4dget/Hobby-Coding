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

def check(n, k):
	""" Return True iff k%2**n == 2**n -1 """
	overflow = 2**n
	max = overflow - 1
	
	return k%overflow == max

def run(infilepath, outfilepath):
	output = open(outfilepath, 'w')
	with open(infilepath, 'r') as input:
		T = int(input.readline().strip())
		for t in range(T):
			n, k = [int(i.strip()) for i in input.readline().strip().split()]
			output.write("Case #%d: %s\n" %(t+1, ["OFF", "ON"][int(check(n,k))]))
			
	output.close()
			
if __name__ == "__main__":
	print 'starting'
	infilepath = 'A-large-practice.in'
	outfilepath = 'A-large-practice.out'
	
	run(infilepath, outfilepath)
	
	print 'done'