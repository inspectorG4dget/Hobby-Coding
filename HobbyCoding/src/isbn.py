'''
Created on Sep 25, 2010

@author: ashwin
'''

def valid10(isbn):
	"""Return True iff the input string is a valid ISBN-10"""
	sum = 0
	for i in range(0, 10):
		weight = 10 - i
		digit = int(isbn[i])
		sum += digit*weight
		
	return not sum%11
	
def generateIsbn10(n):
	"""Generate all valid ISBN-10 < n"""
	curr = 0
	for _ in range(n):
		done = False
		while not done:
			prospect = "%010d" %curr
			if valid10(prospect):
				done = True
				yield prospect
			curr += 1