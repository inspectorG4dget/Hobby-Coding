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

def sms(msg):
	answer = ''
	mapping = {'a':'2',
	'b':'22',
	'c':'222',
	'd':'3',
	'e':'33',
	'f':'333',
	'g':'4',
	'h':'44',
	'i':'444',
	'j':'5',
	'k':'55',
	'l':'555',
	'm':'6',
	'n':'66',
	'o':'666',
	'p':'7',
	'q':'77',
	'r':'777',
	's':'7777',
	't':'8',
	'u':'88',
	'v':'888',
	'w':'9',
	'x':'99',
	'y':'999',
	'z':'9999',
	' ':'0'
	}
	
	for char in msg:
		key = mapping[char]
		if answer.endswith(key[0]):
			answer += ' '
		answer += key
	return answer

def run(infilepath, outfilepath):
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	for case in xrange(1, int(infile.readline().strip())+1):
		outfile.write("Case #%d: %s\n" %(case, sms(infile.readline().rstrip('\n'))) )
		
	
if __name__ =="__main__":
	print 'starting'
	infilepath = 'C-large-practice.in'
	outfilepath = 'C-large-practice.out'
	run(infilepath, outfilepath)
	print 'done'