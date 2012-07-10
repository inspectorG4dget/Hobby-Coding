'''
Created on Jul 17, 2011

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
from string import ascii_lowercase as lowerchars
from collections import defaultdict
from time import sleep
from lxml import etree
from wap import *

class Hangman:
	
	VOWELS = set('aeiou')
	CONSONATS = set('bcdfghjklmnpqrstvwxyz')
	
	def __init__(self, length):
		self.APP_ID = '7HJ2WW-XKQEHAYLLW'
		self.engine = WolframAlphaEngine(self.APP_ID, 'http://api.wolframalpha.com/v2/query?')
		self.length = length	# the length of the word to be guessed
		self.answer = ['_']*length	# internal representation of the word with "_" representing unknown character
		self.chars = lowerchars		# a-z
		self.hang = 0	# number of wrong guesses so far
		self.done = False
		self.collocations = [('cgpstw', 'h'), ('q', 'u')]	# characters that appear together
		self.endings = {3:['ing', 'ion', 'ize', 'ism', 'ist', 'est', 'ify', 'ise', 'ity']}	#common word endings by length
		self.checkWolfram = False
		self.wolframWritable = True
#		self.WORD = list("diarizing")	# for testing purposes only	

	def SERVER(self, guess):
		"""emulates human player"""
#		WORD = list("apple")
#		if guess in WORD:
#			return [i+1 for i,w in enumerate(WORD) if w==guess]
		if raw_input("Is '%s' in the word? (y/n): " %guess) != 'y':
			return []
		else:
			return [int(i) for i in raw_input("What positions of the word are '%s'? " %guess).split()]
		
	
	def play(self):
		while not self.done:
			self.makeGuess()
			
	def getWordsFromWolfram(self):
		"""Get all words from WolframAlpha that they match the internal representation of the answer"""
		
		print "wolfram"
		reply = self.engine.PerformQuery(self.engine.CreateQuery("+".join(self.answer)))
		root = etree.XML(reply)
		answer = map(lambda x : x.replace(" ", '').replace("|", ''), filter(bool, map(lambda x : x.strip(), etree.tostring(root, method='text').split('\n'))))[1:]
		if answer == ['(nocompletecommonwords)']:
			return []
		else:
			return filter(lambda x: all([char in self.chars+''.join(self.answer) for char in x]), answer)
			
	def getProbabilities(self):
		"""Get the probabilities that each of the letters of the alphabet are in any word in words"""
	
		numWords = len(self.words)
		d = {}
		for char in self.chars:
			numwords = len(filter(lambda x : char in x, self.words))
			d[char] = float(numwords)/numWords if numwords else 0
			
		return d
	
	def getVarPostions(self):
		"""Return a dictionary where the keys are caharacters from self.chars adn the values are sets of ints, 
		where each int is an index at which char occurs in any word in self.words"""
		
		answer = defaultdict(set)
		for char in self.chars:
			for word in self.words:
				answer[char].update([i for i,w in enumerate(word) if w==char])
		return answer

	def nextGuess(self):
		"""Propose the next character to guess, based on word endings, collocations, etc"""
		
		for char in 'rstlne':
			if char in char in self.chars:
				self.chars.replace(char, '')
				return char
		if self.wolframWritable:
			self.checkWolfram = True
			self.wolframWritable = False
			
		for endlen, ends in self.endings.iteritems():
			ending = ''.join(self.answer)[-endlen:]
			for end in ends:
				if 	all([char in self.answer or char in self.chars for char in end]) and \
					all([(ending[i] is '_' and end[i] not in self.answer) or ending[i] is end[i] for i in range(len(end))]):
					
					for char in end:
						if char in self.chars:
							self.chars.replace(char, '')
							return char

		if self.checkWolfram:
			self.words = self.getWordsFromWolfram()
			self.checkWolfram = False
		if hasattr(self, 'words') and self.words:

			guess = ''
			count = 0
			for char, poss in self.getVarPostions().iteritems():
				if len(poss) > count:
					guess = char
					count = len(poss)
			if len([k for k,v in self.getVarPostions().iteritems() if len(v)==count]) > 0.5*len(self.words):
				diff = 1
				guess = ''
				for char, prob in self.getProbabilities().iteritems():
					if abs(0.5-prob) < diff:
						guess = char
						diff = abs(0.5-prob)
				self.chars.replace(guess, '')
			return guess
	
		for collocation in self.collocations:
			firsts = (i for i,x in enumerate(self.answer[:-1]) if x in collocation[0])
			seconds = (i for i,x in enumerate(self.answer[1:]) if x == collocation[1])
			
			for i in firsts:
				if self.answer[i+1] == '_':
					for char in collocation[1]:
						if char in self.chars:
							self.chars.replace(char, '')
							return char
				
			for i in seconds:
				if self.answer[i-1] == '_':
					for i, char in firsts:
						if char in self.chars:
							self.chars.replace(char, '')
							return char
		
		for i, w in enumerate(self.answer[:-3]):
			if w in self.CONSONATS and self.answer[i+2] in self.CONSONATS and self.answer[i+1]=="_":
				for v in (v for v in self.VOWELS if v in self.chars):
					self.chars.replace(v, '')
					return v
				if 'y' in self.chars:
					self.chars.replace('y', '')
					return 'y'
		
		
	def makeGuess(self):
		"""Get the next guess and offer it as a guess. 
		Change the internal representation of the answer, self.fragments and self.words according to whether the guess was correct"""

		g = self.nextGuess()
		print "guessing", g
		if not g:
			print "I give up!"
			print "You got me as far as '%s'" %('HANGMAN'[: self.hang-1])
			self.done = True
		else:
			correct = self.SERVER(g)
			if correct:
				for i in correct:
					self.answer[i-1] = g
				if '_' not in self.answer:
					self.done = True
					print "the word is %s" %''.join(self.answer)
					print "You got me as far as '%s'" %('HANGMAN'[: self.hang])
					
				if hasattr(self, 'words'):
					print self.words
					self.words = map(lambda x: x.replace(g, "_"), filter(lambda x : x.count(g)==len(correct) and all([x[c-1]==g for c in correct]), self.words))
					if len(self.words) == 1:
						for i,char in enumerate(self.words[0]):
							if char != "_":
								self.answer[i] = char
						print "the word is", ''.join(self.answer)
						self.done = True 
			else:
				self.hang += 1
				if hasattr(self, 'words'):
					self.words = filter(lambda x : g not in x, self.words)
					
			self.chars = self.chars.replace(g, '')
		print ' '.join(self.answer), '/', "HANGMAN"[:self.hang], '\n'
		sleep(1)
			
def runtest(numiterations=0):
	allwords = (w.strip() for w in open('hangmanwords copy', 'r'))
	if numiterations:
		for _ in xrange(numiterations):
			w = allwords.next()
			h = Hangman(len(w), 'hangmanwords')
			h.WORD = list(w)
			h.play()
			yield ((''.join(h.answer), h.chars, h.hang))
	else:
		for i,w in enumerate(allwords):
			h = Hangman(len(w), 'hangmanwords')
			h.WORD = list(w)
			h.play()
			print i,
			yield ((''.join(h.answer), h.chars, h.hang))

if __name__ == "__main__":
#	h = Hangman(len('_understand'))
#	h.answer = list('_understand')
#	h.getWordsFromWolfram()
	h = Hangman(len('factum'))
	h.play()
#	for i in runtest(): print i[-1]
