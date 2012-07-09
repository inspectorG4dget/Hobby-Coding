'''	
Created on Nov 20, 2010

@author: ashwin
'''
import re

def readFile(filepath):
	with open(filepath, 'r') as f:
		L, D, N = f.readline().strip().split()
		L, D, N = int(L), int(D), int(N)
		corpus = []
		tests = []
		
		for _ in range(D):
			corpus.append(f.readline().strip())
		
		for _ in range(N):
			tests.append(f.readline().strip())
		
		return corpus, tests

def run(infilepath, outfilepath): 
	with open(outfilepath, 'w') as f:
		corpus, tests = readFile(infilepath)
		regexes = ["^" + i.replace("(", '[').replace(")", ']') + "$" for i in tests]
		for i in range(len(regexes)):
			count = len([_ for _ in filter(lambda x : re.search(regexes[i], x).group(0) if re.search(regexes[i], x) else None, corpus) if _])
			f.write("Case #%d: %d\n" %(i+1, count))
		
if __name__ == "__main__":
	print "starting"
	infilepath = 'A-small-practice.in'
	outfilepath = 'A-small-practice.out'
	run(infilepath, outfilepath)
	print "done"