'''
Created on Dec 9, 2010

@author: ashwin
'''

def highestSum(L):
	""" L is a list of 10 lists. Each sublist contains 10 ints.
		These lists are viewed as a grid
		Return the highest sum of any row/column in the grid"""
	
	curr = 0
	for row in L:
		curr = sum(row) if sum(row) > curr else curr
		
	for col in zip(*L):
		curr = sum(col) if sum(col) > curr else curr
		
	return curr

if __name__ == "__main__":
	import sys
	L = []
	for i in range(10):
		L.append([int(i) for i in sys.stdin.readline().strip().split()])
	print highestSum(L)