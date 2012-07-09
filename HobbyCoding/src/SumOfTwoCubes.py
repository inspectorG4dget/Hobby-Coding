'''
Created on Sep 17, 2010

@author: ashwin
'''

def resolve(n):
	"""The input n is an integer. This function will returns a tuple. 
		If n is expressible as the sum of two cubes, the returned tuple will contain the two integers, 
		the sum of whose cubes is n. If no two such integers exist, then an empty tuple is returned"""
		
	for i in range(n):
		j = -1
		sum = i**3
		while sum < n:
			j += 1
			sum = (i**3) + (j**3)

		if sum == n:
			return (i, j)
	return ()

def run(n):
	answer = resolve(n)
	if answer:
		print "%d can be expressed as the sum of the cubes of %d and %d" %(n, answer[0], answer[1])
	else:
		print "%d cannot be expressed as the sum of two cubes" %n
		
if __name__ == "__main__":
	while True:
		try:
			input = int(raw_input("Enter a number: "))
			run(input)
		except ValueError:
			print "Your input was not a number. Try again."