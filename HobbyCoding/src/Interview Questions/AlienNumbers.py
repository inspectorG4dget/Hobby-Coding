'''
Created on Nov 13, 2011

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

def alienToDec(n, alienDigits):
	answer = 0
	base = len(alienDigits)
	for char in n:
		answer *= base
		answer += alienDigits.index(char)
	
	return answer

def decToAlien(n, alienDigits):
	if n == 0:
		return ''
	else:
		base = len(alienDigits)
		return decToAlien(n/base, alienDigits) + alienDigits[n%base] 

def alienToAlien(srcNum, srcDigits, destDigits):
	dec = alienToDec(srcNum, srcDigits)
	return decToAlien(dec, destDigits)
	
if __name__ == "__main__":
	print alienToDec('1011', '01')
	print decToAlien(11, '01')
	print alienToAlien('1011', '01', '012')