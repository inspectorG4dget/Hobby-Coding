'''
Created on Jan 19, 2011

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

def findb(a, c):
#	answer = 's'
#	diff = 's'
#	for b in range(c+1):
#		d = abs((a*b)-c)
#		if d < diff:
#			answer = b
#			diff = d
#	return answer

	return (c/a)+1 if (float(c)/a)%1 > 0.5 else c/a

def run(infilepath, outfilepath):
	input = open(infilepath, 'r')
	output = open(outfilepath, 'w')
	T = int(input.readline().strip())
	for _ in range(T):
		a, c = [int(i) for i in input.readline().strip().split()]
		output.write("%d\n" %findb(a,c))
		
if __name__ == "__main__":
	print 'starting'
	
	infilepath = 'input.txt'
	outfilepath = 'output.txt'
	run(infilepath, outfilepath)
#	print findb(24, 426)

	print 'done'