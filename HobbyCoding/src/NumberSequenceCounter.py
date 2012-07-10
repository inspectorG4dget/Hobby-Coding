'''
Created on Feb 6, 2011

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

def generate(n=0):
	print '1'
	i = next('1')
	print i
	if n:
		for _ in range(n-1):
			i = next(i)
			print i#, len(i)
	else:
		while True:
			i = next(i)
			print i#, len(i)
			
def next(n):
	answer = ''
	i = 0
	while i<len(n):
		i0 = n[i]
		i1= None
		i2 = None
		if i+1<len(n):
			i1 = n[i+1]
			if i+2<len(n):
				i2 = n[i+2]
		if i0 == i1:
			if i1 == i2:
				answer += '3'+i0
				i += 2
			else:
				answer += '2'+i0
				i += 1
		else:
			answer += '1'+i0
		
		i += 1
	return answer	
		
if __name__ == "__main__":
	generate(50)