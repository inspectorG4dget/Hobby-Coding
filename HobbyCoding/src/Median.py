'''
Created on Feb 7, 2011

@author: ashwin
'''

def median(L1, L2):
	c1, c2 = L1[len(L1)/2], L2[len(L2)/2]
	if len(L1) == 1:
		return min(L1+L2)
	if c1>c2:
		return median (L1[:(len(L1)/2)], L2[(len(L2)/2)+1:])
	elif c1<c2:
		return median (L1[(len(L1)/2)+1:], L2[:(len(L2)/2)])

if __name__ == "__main__":
	print median([2,13,21,34], [3,5,8,55])