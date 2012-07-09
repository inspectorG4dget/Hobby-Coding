'''
Created on May 19, 2011

@author: ashwin
'''

def rev(L):
	L.reverse()
	return L

def run(infilepath, outfilepath):
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	for case in xrange(1, int(infile.readline().strip())+1):
		outfile.write("Case #%d: %s\n" %(case, ' '.join(rev(infile.readline().strip().split()))) )
		
	infile.close()
	outfile.close()
	
if __name__ == "__main__":
	print 'starting'
	infilepath = 'B-large-practice.in'
	outfilepath = 'B-large-practice.out'
	run(infilepath, outfilepath)
	print 'done'