'''
Created on Sep 24, 2010

@author: ashwin
'''


def alienToDec(n, alienDigits):
	answer = 0
	for i in range(-1, -1*(len(n)+1), -1):
		answer += alienDigits.index(n[i]) * (len(alienDigits)**((i+1)*-1) )
	
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
#	print alienToDec('1011', '01')
	print decToAlien(11, '01')