'''
Created on Jul 15, 2011

@author: ashwin
'''
from string import ascii_lowercase as lowerchars

class Hangman:
	def __init__(self, infilepath, length):
		self.filepath = infilepath
		self.words = filter(lambda x: len(x) == length, self.__readword__(infilepath))
		self.backup = self.words[:]
		self.fragments = self.words[:]
		self.answer = ['-']*length
		self.chars = lowerchars
		self.hang = 0
		self.done = False
		self.endings = {3:['ing', 'ion', 'ize', 'ism', 'ist', 'est', 'ify', 'ise', 'ity']}
		
	def __readword__(self, infilepath):
		f = open(infilepath, 'r')
		for line in f:
			yield line.strip()
			
	def getWords(self, infilepath, length):
		words = self.__readword__(infilepath)
		word = words.next()
		print word
		try:
			while len(word) < length:
				word = words.next()
			while len(word) < length+1:
				yield word
				word = words.next()
			yield
		except:
			yield  
	
	def nextGuess(self):
		
		for endlen, ends in self.endings.iteritems():
			ending = ''.join(self.answer)[-endlen:]
			for end in ends:
				if 	all([char in self.answer or char in self.chars for char in end]) and \
					all([(ending[i] is '-' and end[i] not in self.answer) or ending[i] is end[i] for i in range(len(end))]):
					
					for char in end:
						if char in self.chars:
							return char
		
		diff = 1
		guess = ''
		for char, prob in self.getProbabilities().iteritems():
			if abs(0.5-prob) < diff and char in ''.join(self.fragments):
				guess = char
				diff = abs(0.5-prob)
		return guess
	
	def makeGuess(self):
		"""Get the next guess and offer it as a guess. If the """
		g = self.nextGuess()
		if not g:
			print "I give up!"
			print "Wait, was it one of these:\n\t%s" %"\n\t".join(self.backup)
			self.done = True
			if raw_input("Any of those? (y/n): ").strip() != 'y':
				open(self.filepath, 'a').write('\n%s\n' %raw_input("What was the word?: ").strip())
			else:
				print "Ha! You gave me wrong clues, and I still won!\nYou got me as far as '%s'" %'HANGMAN'[: self.hang-1]
		else:
			correct = raw_input('is "%s" in the word?: ' %g) == 'y'
			if correct:
				locations = raw_input('where all is this character located: ').split()
				for i in locations:
					self.answer[int(i)-1] = g
				self.fragments = map(lambda x : x.replace(g, ''), filter(lambda x: x.count(g)>=len(locations), self.fragments))
				self.words = filter(lambda x : g in x, self.words)
				
				if '-' not in self.answer:
					self.done = True
					print "the word is %s" %''.join(self.answer)
				elif len(self.words) == 1:
					self.done = True
					print "the word is '%s'\nYou got me as far as '%s'" %(''.join(self.words[0]), 'HANGMAN'[: self.hang-1])
			else:
				self.hang += 1
				self.words = filter(lambda x : g not in x, self.words)
				self.fragments = filter(lambda x : g not in x, self.fragments)
			self.chars = self.chars.replace(g, '')
			if self.words:
				self.backup = self.words[:]
		
	def play(self):
		while not self.done:
			self.makeGuess()
	
	def getProbabilities(self):
		"""Get the probabilities that each of the letters of the alphabet are in any word in words"""
	
		numWords = len(self.words)
		d = {}
		for char in self.chars:
			numwords = len(filter(lambda x : char in x, self.words))
			d[char] = float(numwords)/numWords if numwords else 0
			
		return d
	
if __name__ == "__main__":
	infilepath = 'hangmanwords'
	h = Hangman(infilepath, 7)
	h.play()