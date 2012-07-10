'''
Created on Jan 21, 2012

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


def spiral(n, pad=0):
	x, y = 0, 0
	
	if n <= 0:
		return None
	
	while x < n:
		print x+pad, y+pad
		x += 1

	x -= 1
	y += 1
	while y < n:
		print x+pad, y+pad
		y += 1
	
	x -= 1
	y -= 1
	while x >= 0:
		print x+pad, y+pad
		x -= 1
	
	x += 1
	y -= 1
	while y > 0:
		print x+pad, y+pad
		y -= 1
	
	return spiral(n-2, pad+1)

if __name__ == "__main__":
	spiral(3)