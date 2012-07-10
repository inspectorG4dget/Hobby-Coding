'''
Created on Jan 23, 2012

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

hacker = "HACKERCUP"

def getLetters(line):
	answer = dict((c, 0) for c in hacker)
	for char in line.strip():
		if char in answer:
			answer[char] += 1
	
	answer["C"] /= 2
	return answer

def countHacker(letters):
	return min(letters.values())

def run(infilepath, outfilepath):
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	T = int(infile.readline())
	for t in xrange(1, T+1):
		chars = getLetters(infile.readline())
		outfile.write("Case #%d: %d\n" %(t, countHacker(chars)))
	
	infile.close()
	outfile.close()

if __name__ == "__main__":
	infilepath = '/home/ashwin/Downloads/alphabet_soup.txt'
	outfilepath = '/home/ashwin/Downloads/alphabet_soup_out.txt'
	
	print 'starting'
	run(infilepath, outfilepath)
	print 'done'