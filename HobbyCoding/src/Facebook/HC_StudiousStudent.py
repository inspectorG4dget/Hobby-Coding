'''
Created on Jan 7, 2011

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

def listall(L, w=''):
	""" Given a list of strings, return a list containing every possible concatenation of all strings"""
	
	if not L:
		answer.append(w)
	else:
		for word in L:
			M = L[:]
			M.remove(word)
			listall(M, w+word)
	
def run(infilepath, outfilepath):
	fin = open(infilepath, 'r')
	fout = open(outfilepath, 'w')
	
	N = int(fin.readline().strip())
	for _ in range(N):
		L = fin.readline().strip().split()[1:]
		global answer
		answer = []
		listall(L)
		fout.write("%s\n" %min(answer))
		
	fin.close()
	fout.close()
	
if __name__ == "__main__":
	print 'starting'
	infilepath = "testin.txt"
	outfilepath = "testout.txt"
	run(infilepath, outfilepath)
	print 'done'