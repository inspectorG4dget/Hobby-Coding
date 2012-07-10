'''
Created on May 19, 2011

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

def rev(L):
	L.reverse()
	return L

def run(infilepath, outfilepath):
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	for case in xrange(1, int(infile.readline().strip())+1):
		outfile.write("Case #%d: %s\n" %(case, ' '.join(rev(infile.readline().strip().split()))) )
		
	infile.close()
	outfile.close()
	
if __name__ == "__main__":
	print 'starting'
	infilepath = 'B-large-practice.in'
	outfilepath = 'B-large-practice.out'
	run(infilepath, outfilepath)
	print 'done'