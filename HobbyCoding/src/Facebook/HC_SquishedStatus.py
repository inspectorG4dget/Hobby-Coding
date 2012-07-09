'''
Created on Jan 28, 2012

@author: ashwin
'''

def generateStatuses(enc, max, answer=[]):
	""" Return the number of encoded messages. The highest encoding is max"""
	
#	if not enc:
#		return answer
	if enc:
		codes = []
		i = 1
		while int(enc[:i]) <= max and i < len(enc)	: 
			codes.append(enc[:i])
			i += 1
		
		for code in codes:
			answer[0] += 1
			generateStatuses(enc[len(code):], max, answer)
			

def run(infilepath, outfilepath):
	infile = open(infilepath)
	outfile = open(outfilepath, 'w')
	
	N = int(infile.readline())
	for n in xrange(1, N+1):
		print n, '/', N
		max = int(infile.readline())
		enc = infile.readline().strip()
		answer = [0]
		generateStatuses(enc, max, answer)
		
		outfile.write("Case #%d: %d\n" %(n, answer[0]))

if __name__ == "__main__":
	print 'starting'
	infilepath = '/home/ashwin/Downloads/input.txt'
	outfilepath = '/home/ashwin/Downloads/output.txt'
	run(infilepath, outfilepath)
	print 'done'