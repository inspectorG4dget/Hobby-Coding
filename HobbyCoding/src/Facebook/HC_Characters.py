'''
Created on Jan 20, 2011

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

def run(infilepath, outfilepath):
	
	input = open(infilepath, 'r')
	output = open(outfilepath, 'w')
	
	T = int(input.readline().strip())
	for _ in range(T):
		output.write("%d\n" %len(set(input.readline().strip().lower())))
		
	input.close()
	output.close()

if __name__ == "__main__":
	print 'starting'
	
	infilepath = 'input.txt'
	outfilepath = 'output.txt'
	run(infilepath, outfilepath)
	
	print 'done'