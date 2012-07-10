'''
Created on Jan 29, 2011

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

def factor(F, G, H):
	if not F or F==[0]: return H
	elif len(G) > len(F): return "no solution"
	else:
		H.append(float(F[0])/G[0])
		for i in range(1, len(G)):
			F[i] -= G[i]*H[-1]
		return factor(F[1:], G, H)
		
def run(infilepath):
	f = open(infilepath, 'r')
	N = int(f.readline().strip())
	for i in range(N):
		F = [int(i) for i in f.readline().strip().split()][1:]
		G = [int(i) for i in f.readline().strip().split()][1:]
		print factor(F, G, [])
		
	f.close()
	
if __name__ == "__main__":
	run('testin.txt')