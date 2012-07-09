from math import log
def collatz(n):
	print n
	if log(n,2) == int(log(n,2)): return True
	else:
		n = (3*n)+1 if n%2 else n/2
		return collatz(n)

if __name__ == "__main__":
	for i in range(3, 100, 2):
		print collatz(i)
		print "="*40
