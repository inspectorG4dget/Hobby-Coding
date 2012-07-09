'''
Created on Dec 30, 2010

@author: ashwin
'''

from itertools import product as prod
def indices(word, text, L=[]):
	for char in word:
		L.append(findall(char, text))
	
	return L

def findall(char, text):
	answer = []
	try:
		while text:
			i = text.index(char)
			answer.append(i)
			text = text[i+1 :]
			
	except ValueError:
		return answer
	
def validate(L):
	L = list(L)
	M = L[:]
	M.sort()
	return L==M

def count(L):
	applicants = prod(*L)
	return len(filter(lambda L: validate(L), [i for i in applicants])) % 10000

def run(infilepath, outfilepath):
	with open(infilepath, 'r') as input:
		output = open(outfilepath, 'w')
		N = int(input.readline().strip())
		for i in range(N):
			x = i+1
			text = input.readline()
			answer = count(indices('welcome to code jam', text))
			output.write("Case #%d: %04d\n" %(x, answer))
			
		output.close()
		
if __name__ == "__main__":
	print 'starting'
	
	infilepath = 'C-small-practice.in'
	outfilepath = 'C-small-practice.out'
	run(infilepath, outfilepath)
	
	print 'done'