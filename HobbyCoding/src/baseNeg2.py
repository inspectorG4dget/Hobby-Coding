'''
Created on Sep 22, 2010

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

def convertBaseNeg2(n):
	
	g = generateStrings()
	candidate = g.next()
	done = False
	while not done:
		if negBinToDec(candidate) == n:
			done = True
			return candidate
		else:
			candidate = g.next()
			
def negBinToDec(s):
	i = 0
	s = s[::-1]
	answer = 0
	while i < len(s):
		answer += int(s[i]) * ((-2)**i)
		i += 1
	return answer

def generateStrings():
	i = -1
	while True:
		i += 1
		yield decToBin(i)
		
def decToBin(n):
	if n==0: return''
	else:
		return decToBin(n/2) + str(n%2)