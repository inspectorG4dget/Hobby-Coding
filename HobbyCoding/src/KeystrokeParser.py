'''
Created on Feb 2, 2011

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

def shift(s):
	LOWER = '`1234567890-=[];\'\,./'
	UPPER = '~!@@#$%^&*()_+{}:"|<>?'
	
	if s.isalpha():
		return s.upper()
	else:
		return UPPER[LOWER.index(s)]

def parse(input):
	input = input.split("[BACKSPACE]")
	answer = ''
	i = 0
	while i<len(input):
		s = input[i]
		if not s:
			pass
		elif i+1<len(input) and not input[i+1]:
			s = s[:-1]
		else:
			answer += s
			i += 1
			continue
		answer += s[:-1]
		i += 1
		
	return ''.join(shift(i[0])+i[1:] for i in answer.split("[SHIFT]") if i)

if __name__ == "__main__":
	print parse("[SHIFT]this isrd[BACKSPACE][BACKSPACE] an example file[SHIFT]1")