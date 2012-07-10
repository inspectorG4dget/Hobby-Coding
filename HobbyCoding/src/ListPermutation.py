'''
Created on Oct 4, 2010

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


def permute(L):
	if L == []:
		return []
	else:
		for i in range(len(L)-1):
			a = [L[i]]
			b = L[:i]
			c = L[i+1 :]
			print "B:", b
			print "C:", c
			d = b + c
			return a + permute(d)

def includeMembers(L):
	if not L:
		return L
	else:
		for i in L[0]:
			includeMembers(L[1:])[-1] += i
		
if __name__ == "__main__":
	print includeMembers(['asdf', 'jkl;'])