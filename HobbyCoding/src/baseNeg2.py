'''
Created on Sep 22, 2010

@author: ashwin
'''

def convertBaseNeg2(n):
	
	g = generateStrings()
	candidate = g.next()
	done = False
	while not done:
		if negBinToDec(candidate) == n:
			done = True
			return candidate
		else:
			candidate = g.next()
			
def negBinToDec(s):
	i = 0
	s = s[::-1]
	answer = 0
	while i < len(s):
		answer += int(s[i]) * ((-2)**i)
		i += 1
	return answer

def generateStrings():
	i = -1
	while True:
		i += 1
		yield decToBin(i)
		
def decToBin(n):
	if n==0: return''
	else:
		return decToBin(n/2) + str(n%2)