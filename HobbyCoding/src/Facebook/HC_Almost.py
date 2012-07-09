'''
Created on Jan 19, 2011

@author: ashwin
'''

def findb(a, c):
#	answer = 's'
#	diff = 's'
#	for b in range(c+1):
#		d = abs((a*b)-c)
#		if d < diff:
#			answer = b
#			diff = d
#	return answer

	return (c/a)+1 if (float(c)/a)%1 > 0.5 else c/a

def run(infilepath, outfilepath):
	input = open(infilepath, 'r')
	output = open(outfilepath, 'w')
	T = int(input.readline().strip())
	for _ in range(T):
		a, c = [int(i) for i in input.readline().strip().split()]
		output.write("%d\n" %findb(a,c))
		
if __name__ == "__main__":
	print 'starting'
	
	infilepath = 'input.txt'
	outfilepath = 'output.txt'
	run(infilepath, outfilepath)
#	print findb(24, 426)

	print 'done'