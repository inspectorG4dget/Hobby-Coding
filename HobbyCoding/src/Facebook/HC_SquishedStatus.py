'''
Created on Jan 28, 2012

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

def generateStatuses(enc, max, answer=[]):
	""" Return the number of encoded messages. The highest encoding is max"""
	
#	if not enc:
#		return answer
	if enc:
		codes = []
		i = 1
		while int(enc[:i]) <= max and i < len(enc)	: 
			codes.append(enc[:i])
			i += 1
		
		for code in codes:
			answer[0] += 1
			generateStatuses(enc[len(code):], max, answer)
			

def run(infilepath, outfilepath):
	infile = open(infilepath)
	outfile = open(outfilepath, 'w')
	
	N = int(infile.readline())
	for n in xrange(1, N+1):
		print n, '/', N
		max = int(infile.readline())
		enc = infile.readline().strip()
		answer = [0]
		generateStatuses(enc, max, answer)
		
		outfile.write("Case #%d: %d\n" %(n, answer[0]))

if __name__ == "__main__":
	print 'starting'
	infilepath = '/home/ashwin/Downloads/input.txt'
	outfilepath = '/home/ashwin/Downloads/output.txt'
	run(infilepath, outfilepath)
	print 'done'