'''
Created on Feb 7, 2011

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

def median(L1, L2):
	c1, c2 = L1[len(L1)/2], L2[len(L2)/2]
	if len(L1) == 1:
		return min(L1+L2)
	if c1>c2:
		return median (L1[:(len(L1)/2)], L2[(len(L2)/2)+1:])
	elif c1<c2:
		return median (L1[(len(L1)/2)+1:], L2[:(len(L2)/2)])

if __name__ == "__main__":
	print median([2,13,21,34], [3,5,8,55])