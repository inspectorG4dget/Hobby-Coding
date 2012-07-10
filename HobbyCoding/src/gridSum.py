'''
Created on Dec 9, 2010

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

def highestSum(L):
	""" L is a list of 10 lists. Each sublist contains 10 ints.
		These lists are viewed as a grid
		Return the highest sum of any row/column in the grid"""
	
	curr = 0
	for row in L:
		curr = sum(row) if sum(row) > curr else curr
		
	for col in zip(*L):
		curr = sum(col) if sum(col) > curr else curr
		
	return curr

if __name__ == "__main__":
	import sys
	L = []
	for i in range(10):
		L.append([int(i) for i in sys.stdin.readline().strip().split()])
	print highestSum(L)