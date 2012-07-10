'''
author: ashwin

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

def printTime(h, m):
	face = {
			0: "        o",             \
			1: "    o       o",         \
			2: " o             o",     \
			3: "o               o",    \
			4: " o             o",     \
			5: "    o       o",         \
			6: "        o",         \
			}
	h %= 12
	m /= 5

	if 0 <= h <= 6:
		face[h] = face[h][:-1] + 'h'
	else:
		face[12-h] = face[12-h].replace('o', 'h', 1)

	if 0 <= m <= 6:
		temp = list(face[m])
		temp[-1] = 'x' if temp[-1] == 'h' else 'm'
		face[m] = ''.join(temp)
		
	else:
		temp = list(face[12-m])
		i = [i for i in range(len(temp)) if temp[i]!=' '][0]
		temp[i] = 'x' if temp[i]=='h' else 'm'
		face[12-m] = ''.join(temp)

	print '\n\n'.join(face.values())

def run(digitime):
	h, m = digitime.split(':')
	printTime(int(h), int(m))

if __name__ == "__main__":
	import sys
	run(sys.stdin.realine().strip())