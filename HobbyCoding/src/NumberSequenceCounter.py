'''
Created on Feb 6, 2011

@author: ashwin
'''

def generate(n=0):
	print '1'
	i = next('1')
	print i
	if n:
		for _ in range(n-1):
			i = next(i)
			print i#, len(i)
	else:
		while True:
			i = next(i)
			print i#, len(i)
			
def next(n):
	answer = ''
	i = 0
	while i<len(n):
		i0 = n[i]
		i1= None
		i2 = None
		if i+1<len(n):
			i1 = n[i+1]
			if i+2<len(n):
				i2 = n[i+2]
		if i0 == i1:
			if i1 == i2:
				answer += '3'+i0
				i += 2
			else:
				answer += '2'+i0
				i += 1
		else:
			answer += '1'+i0
		
		i += 1
	return answer	
		
if __name__ == "__main__":
	generate(50)