'''
Created on Jul 17, 2011

@author: ashwin
'''
from string import ascii_lowercase as lowerchars
from collections import defaultdict, namedtuple
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
		WORD = list("apple")
		if guess in WORD:
			return [i+1 for i,w in enumerate(WORD) if w==guess]
#		if raw_input("Is '%s' in the word? (y/n): " %guess) != 'y':
#			return []
#		else:
#			return [int(i) for i in raw_input("What positions of the word are '%s'? " %guess).split()]
		
	
	def play(self):
		while not self.done:
			self.makeGuess()
			
	def _getWords(self):
		"""Get all words from WolframAlpha that they match the internal representation of the answer"""
		
		print "wolfram"
		reply = self.engine.PerformQuery(self.engine.CreateQuery("+".join(self.answer)))
		root = etree.XML(reply)
		answer = map(lambda x : x.replace(" ", '').replace("|", ''), filter(bool, map(lambda x : x.strip(), etree.tostring(root, method='text').split('\n'))))[1:]
		if answer == ['(nocompletecommonwords)']:
			return []
		else:
			return filter(lambda x: all([char in self.chars+''.join(self.answer) for char in x]), answer)
			
	def getCharStats(self):
		"""	Return a dict (char in self.chars : charStat).
			A charStat is a namedtuple which contains the varPositions and the probabilities"""
		
		answer = {} #defaultdict(lambda : namedtuple('CharacterStats', ["probability", "frequency"]))
		numWords = float(len(self.words))
		for char in self.chars:
			numwords = 0
			locs = set([])
			for word in self.words:
				if char in word:
					numwords += 1
					locs.update([i for i,w in enumerate(word) if w==char])
			answer[char] = namedtuple('CharacterStats', ["probability", "frequency"])
			answer[char].probability = numwords/numWords
			answer[char].frequency = len(locs)
			
		return answer
			
	def _blind(self):
		for char in 'rstlne':
			if char in char in self.chars:
				self.chars.replace(char, '')
				return char
			
	def _checkWolfram(self):
		if self.wolframWritable:
			self.checkWolfram = True
			self.wolframWritable = False
			
	def getWords(self):
		if self.checkWolfram:
			self.words = self._getWords()
			self.checkWolfram = False
			
	def _guessEndings(self):
		for endlen, ends in self.endings.iteritems():
			ending = ''.join(self.answer)[-endlen:]
			for end in ends:
				if 	all([char in self.answer or char in self.chars for char in end]) and \
					all([(ending[i] is '_' and end[i] not in self.answer) or ending[i] is end[i] for i in range(len(end))]):
					
					for char in end:
						if char in self.chars:
							self.chars.replace(char, '')
							return char
						
	def _guessCollocations(self):
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
						
	def _guessVowels(self):
		for i, w in enumerate(self.answer[:-3]):
			if w in self.CONSONATS and self.answer[i+2] in self.CONSONATS and self.answer[i+1]=="_":
				for v in (v for v in self.VOWELS if v in self.chars):
					self.chars.replace(v, '')
					return v
				if 'y' in self.chars:
					self.chars.replace('y', '')
					return 'y'
				
	def _equal(self, L, S):
		""" L and S are either lists or tuples or a combination of both. 
			Return True iff L is a subset of S and S is a subset of L"""
		return set(L) == set(S)
	
	def _calcVariance(self, L):
		mean = float(sum(L))/len(L)
		sqDiffs = sum(map(lambda x: x**2, [i-mean for i in L]))
		return sqDiffs/len(L)
		
	def _findEqual(self, L, S):
		"""S is a list of tuples"""
		for s in S:
			if self._equal(L, s):
				return s
		
	def _aposterioriGuess(self):
		print 'apos:', 
		charstats = defaultdict(dict)
		for char in self.chars:
			for word in self.words:
				positions = tuple((i for i, w in enumerate(word) if w == char))
				# if positions does not exist in charstats[char].keys()
				if all([not self._equal(positions, P) for P in charstats[char]]):
					charstats[char][positions] = 1
				else:
					charstats[char][self._findEqual(positions, charstats[char].keys())] += 1
			charstats[char][tuple([])] = len([word for word in self.words if char not in word])
			
		# now that we have the sizes of all the subsets that each charaacter creates, return the character with the lowest variance
		optchars = self._getOptChars(charstats)
		if len(optchars) > 1:
			return min(optchars, key=lambda x: self._calcVariance(charstats[char].values()))
		else:
#			print optchars
			if optchars:
				return optchars.pop()
			else:
				return ''

	def _getOptChars(self, stats):
		maxs = dict([(char, max(stats[char].itervalues())) for char in stats])
		min_largest_subset = min(maxs.itervalues())
		return filter(lambda char:maxs[char] == min_largest_subset, maxs)

	def _getProbabilities(self):
		"""Get the probabilities that each of the letters of the alphabet are in any word in words"""
	
		numWords = len(self.words)
		d = {}
		for char in self.chars:
			numwords = len(filter(lambda x : char in x, self.words))
			d[char] = float(numwords)/numWords if numwords else 0
			
		return d

	def _halfGuess(self):
		diff = 1
		guess = ''
		for char, prob in self._getProbabilities().iteritems():
			if abs(0.5-prob) < diff and char in ''.join(self.fragments):
				guess = char
				diff = abs(0.5-prob)
		return guess
				
	def _fitsAnswerTemplate(self, word):
		answer = True
		for char in self.answer:
			if  char != "_" and \
				word.count(char) != self.answer.count(char) and \
				any([self.answer[i] != char for i,c in enumerate(word) if c == char]):
				
				answer = False
		return answer
				
	def nextGuess(self):
		"""Propose the next character to guess, based on word endings, collocations, etc"""
		
		g = self._blind()
		if g:
			return g
		else:
			self._checkWolfram()
			g = self._guessEndings()
			if g:
				return g
			else:
				self.getWords()
				self.words = filter(self._fitsAnswerTemplate, self.words)
				self.chars = ''.join(sorted([char for char in self.chars if char in ''.join(self.words)]))
#				if self.checkWolfram:
#					self.words = self.getWords()
#					self.checkWolfram = False
					
				g = self._aposterioriGuess()
				if g:
					return g
				else:
					g = self._guessCollocations()
					if g:
						return g
					else:
						g = self._guessVowels()
						if g:
							return g
						else:
							g = self._halfGuess()
							if g:
								return g
				
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
		sleep(0.25)
			
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
#	h.getWords()
	play_again = True
	while play_again:
#		h = Hangman(int(raw_input("How many letters in your word?: ")))
		h = Hangman(len("apple"))
		h.play()
		play_again = False
#		play_again = raw_input("Play again? (y/n): ") == 'y'
#	for i in runtest(): print i[-1]