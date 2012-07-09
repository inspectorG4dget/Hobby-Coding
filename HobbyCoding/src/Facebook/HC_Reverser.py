'''
Created on Jan 20, 2011

@author: ashwin
'''

def reverse(word, i):
	"""Return the encrypted word"""
	
	if len(word) <= i:
		return word
	else:
		p = len(word)/2
		return reverse(word[p:], i) + reverse(word[:p], i)
	
def encrypt(sentence):
	"""Encrypt each word in the sentence and return the encrypted sentence"""
	
	words = sentence.split()
	answer = []
	
	for i in range(len(words)):
		answer.append(reverse(words[i], i+1))
	
	return ' '.join(answer)

def run(infilepath, outfilepath):
	
	input = open(infilepath, 'r')
	output = open(outfilepath, 'w')
	
	T = int(input.readline().strip())
	for _ in range(T):
		sentence = input.readline().strip()
		output.write("%s\n" %encrypt(sentence))
		
if __name__ == "__main__":
	print 'starting'
	
	infilepath = 'input.txt'
	outfilepath = 'output.txt'
	run(infilepath, outfilepath)
	
	print 'done'