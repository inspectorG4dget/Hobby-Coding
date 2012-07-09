'''
Created on May 19, 2011

@author: ashwin
'''

from itertools import combinations as comb

def pack(L, items):

	for pair in comb(items, 2):
		if not sum(pair) - L:
			one = items.index(pair[0])+1
			items[one-1] = None
			two = items.index(pair[1])+1
			return sorted([one, two])

def run(infilepath, outfilepath):
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	for case in xrange(1, int(infile.readline().strip())+1):
		L = int(infile.readline().strip())
		infile.readline()
		lo, hi = pack(L, [int(i) for i in infile.readline().strip().split()])
		outfile.write("Case #%d: %d %d\n" %(case, lo, hi))
	infile.close()
	outfile.close()
	
if __name__ == "__main__":
	print 'starting'
	infilepath = 'A-large-practice.in'
	outfilepath = 'A-large-practice.out'
	run(infilepath, outfilepath)
	print 'done'