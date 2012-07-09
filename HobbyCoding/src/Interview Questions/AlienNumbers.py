'''
Created on Nov 13, 2011

@author: ashwin
'''

def alienToDec(n, alienDigits):
	answer = 0
	base = len(alienDigits)
	for char in n:
		answer *= base
		answer += alienDigits.index(char)
	
	return answer

def decToAlien(n, alienDigits):
	if n == 0:
		return ''
	else:
		base = len(alienDigits)
		return decToAlien(n/base, alienDigits) + alienDigits[n%base] 

def alienToAlien(srcNum, srcDigits, destDigits):
	dec = alienToDec(srcNum, srcDigits)
	return decToAlien(dec, destDigits)
	
if __name__ == "__main__":
	print alienToDec('1011', '01')
	print decToAlien(11, '01')
	print alienToAlien('1011', '01', '012')