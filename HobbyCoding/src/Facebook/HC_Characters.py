'''
Created on Jan 20, 2011

@author: ashwin
'''

def run(infilepath, outfilepath):
	
	input = open(infilepath, 'r')
	output = open(outfilepath, 'w')
	
	T = int(input.readline().strip())
	for _ in range(T):
		output.write("%d\n" %len(set(input.readline().strip().lower())))
		
	input.close()
	output.close()

if __name__ == "__main__":
	print 'starting'
	
	infilepath = 'input.txt'
	outfilepath = 'output.txt'
	run(infilepath, outfilepath)
	
	print 'done'