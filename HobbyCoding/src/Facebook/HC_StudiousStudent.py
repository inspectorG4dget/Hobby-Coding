'''
Created on Jan 7, 2011

@author: ashwin
'''

def listall(L, w=''):
	""" Given a list of strings, return a list containing every possible concatenation of all strings"""
	
	if not L:
		answer.append(w)
	else:
		for word in L:
			M = L[:]
			M.remove(word)
			listall(M, w+word)
	
def run(infilepath, outfilepath):
	fin = open(infilepath, 'r')
	fout = open(outfilepath, 'w')
	
	N = int(fin.readline().strip())
	for _ in range(N):
		L = fin.readline().strip().split()[1:]
		global answer
		answer = []
		listall(L)
		fout.write("%s\n" %min(answer))
		
	fin.close()
	fout.close()
	
if __name__ == "__main__":
	print 'starting'
	infilepath = "testin.txt"
	outfilepath = "testout.txt"
	run(infilepath, outfilepath)
	print 'done'