'''
Created on Dec 28, 2010

@author: ashwin
'''

def readfile(filepath):
	f = open(filepath, 'r')
	answer = int(f.readline().strip())
	f.close()
	return answer

def writefile(filepath, n):
	f = open(filepath, 'w')
	for i in range(1, n+1):
		if not i%3:
			if not i%5:
				f.write("Hop\n")
			else:
				f.write("Hoppity\n")
		elif not i%5:
			f.write("Hophop\n")
	f.close()
	
def run(infilepath, outfilepath):
	n = readfile(infilepath)
	writefile(outfilepath, n)
	
if __name__ == "__main__":
	print 'starting'
	
	infilepath = raw_input("enter input filepath: ")
	outfilepath = raw_input("enter output filepath: ")
	
	if infilepath and outfilepath:
		run(infilepath, outfilepath)
	
	print 'done'