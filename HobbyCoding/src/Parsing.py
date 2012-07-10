'''
Created on Jan 25, 2011

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

import re
def parse(s):
	s = re.sub("[\{\(\[]", '[', s)
	s = re.sub("[\}\)\]]", ']', s)
	answer = ''
	for i,char in enumerate(s):
		if char == '[':
			answer += char + "'"
		elif char == '[':
			answer += "'" + char + "'"
		elif char == ']':
			answer += char
		else:
			answer += char
			if s[i+1] in '[]':
				answer += "', "
	exec "s=%s" %answer
	return s

if __name__ == "__main__":
	s = parse('(gimme [some {nested [lists]}])')
	print type(s)