'''
Created on Sep 18, 2010

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

def collapse(L):
	""" The input L is a list that contains tuples of various sizes.
		If any tuples have shared elements, 
		exactly one instance of the shared and unshared elements are merged into the first tuple with a shared element.
		This function returns a new list that contain merged tuples and an int that represents how many merges were performed."""
	answer = []
	merges = 0
	seen = []	# a list of all the numbers that we've seen so far
	for t in L:
		tAdded = False
		for num in t:
			pleaseMerge = True
			if num in seen and pleaseMerge:
				answer += merge(t, answer)
				merges += 1
				pleaseMerge = False
				tAdded= True
			else:
				seen.append(num)
		if not tAdded:
			answer.append(t)
		
	return (answer, merges)

def merge(t, L):
	""" The input L is a list that contains tuples of various sizes.
		The input t is a tuple that contains an element that is contained in another tuple in L.
		Return a new list that is similar to L but contains the new elements in t added to the tuple with which t has a common element."""
	answer = []
	while L:
		tup = L[0]
		tupAdded = False
		for i in tup:
			if i in t:
				try:
					L.remove(tup)
					newTup = set(tup)
					for i in t:
						newTup.add(i)
					answer.append(tuple(newTup))
					tupAdded = True
				except ValueError:
					pass
		if not tupAdded:
			L.remove(tup)
			answer.append(tup)
	return answer

def sortByLength(L):
	""" L is a list of n-tuples, where n>0.
		This function will return a list with the same contents as L 
		except that the tuples are sorted in non-ascending order by length"""
	
	lengths = {}
	for t in L:
		if len(t) in lengths.keys():
			lengths[len(t)].append(t)
		else:
			lengths[len(t)] = [(t)]
			
	l = lengths.keys()[:]
	l.sort(reverse=True)
	
	answer = []
	for i in l:
		answer += lengths[i]
	return answer

def MergeThat(L):
	answer, merges = collapse(L)
	while merges:
		answer, merges = collapse(answer)
	return sortByLength(answer)

if __name__ == "__main__":
	print 'starting'
	print MergeThat([(3,4), (18,27), (4,14)])
	print MergeThat([(1,3), (15,21), (1,10), (57,66), (76,85), (66,76)])