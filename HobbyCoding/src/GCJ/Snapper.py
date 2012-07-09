'''
Created on Jan 18, 2011

@author: ashwin
'''

def check(n, k):
	""" Return True iff k%2**n == 2**n -1 """
	overflow = 2**n
	max = overflow - 1
	
	return k%overflow == max

def run(infilepath, outfilepath):
	output = open(outfilepath, 'w')
	with open(infilepath, 'r') as input:
		T = int(input.readline().strip())
		for t in range(T):
			n, k = [int(i.strip()) for i in input.readline().strip().split()]
			output.write("Case #%d: %s\n" %(t+1, ["OFF", "ON"][int(check(n,k))]))
			
	output.close()
			
if __name__ == "__main__":
	print 'starting'
	infilepath = 'A-large-practice.in'
	outfilepath = 'A-large-practice.out'
	
	run(infilepath, outfilepath)
	
	print 'done'