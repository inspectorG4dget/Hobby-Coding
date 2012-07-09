'''
Created on Jan 7, 2011

@author: ashwin
'''
import math

def resolve(n):
	""" This function takes an int as input and returns a set of tuples.
		If the int is expressible as the sum of two squares, the set contains sorted 2-int-tuples.
		The sum of the squares of the ints in each tuple will add up to n"""
		
	answer = set([])
	
	for i in range(int(math.sqrt(n)) +1):
		s1 = i**2
		s2 = n-s1
		if not (math.sqrt(s2) %1):
			a = [s1, s2]
			a.sort()
			answer.add(tuple(a))
			
	return answer

def run(infilepath, outfilepath):
	fin = open(infilepath, 'r')
	fout = open(outfilepath, 'w')
	
	N = int(fin.readline().strip())
	for _ in range(N):
		n = int(fin.readline().strip())
		fout.write("%d\n" %len(resolve(n)))
		
	fin.close()
	fout.close()
	
if __name__ == "__main__":
	print 'starting'
	infilepath = "testin.txt"
	outfilepath = "testout.txt"
	run(infilepath, outfilepath)
	print 'done'