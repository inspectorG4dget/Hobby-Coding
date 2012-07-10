'''
Created on Oct 2, 2011

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

from collections import defaultdict
from pprint import pprint
from random import random, sample
from itertools import chain
#import cPickle

def getBigrams(infilepath):
	answer = defaultdict(float)
	currword = '.'
	total = 0
	with open(infilepath) as f:
		for line in f:
			words = line.strip().lower().replace(',', '').replace('.', '').split()
			if words:
				total += 1
				print total
				answer[(currword, words[0])] = (answer[(currword, words[0])]*(total-1) +1)  /total
				
				for tup in (t for t in answer if t != (currword, words[0])):
					answer[tup] = (answer[tup]*(total-1))/total
	
				for i, word in enumerate(words[0:-1]):
					total += 1
					answer[(word, words[i+1])] = ((answer[(word, words[i+1])] * (total-1)) + 1)/total
					
					for tup in (t for t in answer if t != (word, words[i+1])):
						answer[tup] = (answer[tup]*(total-1))/total
	
				currword = word
	return answer

def getNGrams(infilepath, n, notwords, sentenceEnder, delimiter):
	""" infilepath: path to the inputfile containing all the written works of the author
		n: 1-get unigrams, 2-get bigrams, etc
		notwords: a set containing all strings to not be considered words
		sentenceEnder: in most natural languages, this is '.'
		delimiter: what separates two words (not punctuation - those could be considered words). Newlines are considered delimiters by default
		
		This is the naive way to do this, so it won't work on files that won't fit directly onto main memory """
	
	with open(infilepath) as f:
		contents = ''.join(f.readlines())
		for nw in notwords: contents = contents.replace(nw, '')	# remove all the notwords
		contents = contents.replace('\n', delimiter)
		words = contents.split(delimiter)
		
		answer = defaultdict(int)	# key: ngram, value: how many times does it occur in the text
		for i in (i for i in xrange(len(words) -n+1)):
			answer[words[i:i+n]] += 1
		return answer

def GetNGrams(infilepath, n, notwords, sentenceEnder, delimiter):
	""" infilepath: path to the inputfile containing all the written works of the author
		n: 1-get unigrams, 2-get bigrams, etc
		notwords: a set containing all strings to not be considered words
		sentenceEnder: in most natural languages, this is '.'
		delimiter: what separates two words (not punctuation - those could be considered words). Newlines are considered delimiters by default
		
		This is the smarter way to do this. It holds an N-sized buffer of words in memory """
	
	buffer = Buffer(n)
	answer = defaultdict(int)
	with open(infilepath) as infile:
		for sentence in chain(((i for i in filter(lambda word: word not in notwords, line.replace('\n', delimiter).split(delimiter))) for line in infile)):
			for word in sentence:
				if word:
					buffer.add(word)
					if len(buffer) == n:
						answer[buffer.rep()] += 1
	
	return answer

def nextWord(curr, bigrams):
	bs = [(b,p) for b,p in bigrams if b[0] == curr]
	bs = [b for b in sorted(bs, lambda x,y: y[1]-x[1])]
	bs = (b for b in bs)
	
	answer = bs.next()[1]
	prob = random()
	while prob < 0.5:
		try:
			answer = bs.next()[1]
			prob = random()
		except:
			bs = [(b,p) for b,p in bigrams if b[0] == curr]
			bs = [b for b in sorted(bs, lambda x,y: y[1]-x[1])]
			bs = (b for b in bs)
			continue
	return answer

def generate(bigrams, n=100):
	""" Generate the next n many words, given the bigram probabilities"""
	
	currword = '.'
	for _ in xrange(n):
		print 'yielding'
#		currword = max((tup for tup in bigrams if tup[0]==currword), key=lambda x: bigrams[x])[1]
		currword = nextWord(currword, bigrams)
		yield currword

def Generate(ngrams, delimiter, numwords=100, runningStart=None):
	""" numwords: how many words to generate
		runningStart: startingPoint"""
	n = len(sample(ngrams, 1))
	if not runningStart or len(runningStart.split(delimiter)) < n-1: raise ValueError("Sufficient Running Start not provided")	
	runningStart = runningStart.split(delimiter)
	runningStart = runningStart[len(runningStart-n-1):]
	
	while numwords:
		options = (lambda tup: tup[:-1]==runningStart, ngrams)
		options.sort(key=lambda tup: ngrams[tup])
		options = map(lambda tup: tup[-1], options)
		if random() <= 0.5:	# 0.5 is a parameter that you have to set
			print options[0],
			runningStart.pop(0)
			runningStart.append(options[0])
			numwords -= 1
		else:
			options.append(options.pop(0))
	
	return None

class Buffer:
	def __init__(self, n):
		self.buffer = []
		self.size = n
	
	def __contains__(self, item):
		return item in self.buffer
	
	def __len__(self):
		return len(self.buffer)
	
	def __repr__(self):
		return ' '.join(self.buffer)
	
	def add(self, item):
		self.buffer.append(item)
		if len(self.buffer) > self.size: self.buffer.pop(0)
	
	def rep(self):
		return tuple(self.buffer)

if __name__ == "__main__":
#	pprint(getBigrams('testfile'))
#	for i in generate(getBigrams('Shakespeare.txt'), 200):
#		print i, 
#	out = open("bigrams.txt", 'w')
#	b = getBigrams("Shakespeare.txt")
#	cPickle.dump(b, out)
#	out.close()
#	f = open("bigrams.txt")
#	bigrams = cPickle.load(f)
#	f.close()
#	for i in generate(bigrams, 200): print i
	infilepath = 'blah'
	pprint(GetNGrams(infilepath, 2, set(), '.', ' '))