'''
Created on Jan 23, 2012

@author: ashwin
'''

hacker = "HACKERCUP"

def getLetters(line):
	answer = dict((c, 0) for c in hacker)
	for char in line.strip():
		if char in answer:
			answer[char] += 1
	
	answer["C"] /= 2
	return answer

def countHacker(letters):
	return min(letters.values())

def run(infilepath, outfilepath):
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	T = int(infile.readline())
	for t in xrange(1, T+1):
		chars = getLetters(infile.readline())
		outfile.write("Case #%d: %d\n" %(t, countHacker(chars)))
	
	infile.close()
	outfile.close()

if __name__ == "__main__":
	infilepath = '/home/ashwin/Downloads/alphabet_soup.txt'
	outfilepath = '/home/ashwin/Downloads/alphabet_soup_out.txt'
	
	print 'starting'
	run(infilepath, outfilepath)
	print 'done'