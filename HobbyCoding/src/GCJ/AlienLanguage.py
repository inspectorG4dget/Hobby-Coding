'''	
Created on Nov 20, 2010

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

def readFile(filepath):
	with open(filepath, 'r') as f:
		L, D, N = f.readline().strip().split()
		L, D, N = int(L), int(D), int(N)
		corpus = []
		tests = []
		
		for _ in range(D):
			corpus.append(f.readline().strip())
		
		for _ in range(N):
			tests.append(f.readline().strip())
		
		return corpus, tests

def run(infilepath, outfilepath): 
	with open(outfilepath, 'w') as f:
		corpus, tests = readFile(infilepath)
		regexes = ["^" + i.replace("(", '[').replace(")", ']') + "$" for i in tests]
		for i in range(len(regexes)):
			count = len([_ for _ in filter(lambda x : re.search(regexes[i], x).group(0) if re.search(regexes[i], x) else None, corpus) if _])
			f.write("Case #%d: %d\n" %(i+1, count))
		
if __name__ == "__main__":
	print "starting"
	infilepath = 'A-small-practice.in'
	outfilepath = 'A-small-practice.out'
	run(infilepath, outfilepath)
	print "done"