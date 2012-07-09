'''
Created on Oct 4, 2010

@author: ashwin
'''


def permute(L):
	if L == []:
		return []
	else:
		for i in range(len(L)-1):
			a = [L[i]]
			b = L[:i]
			c = L[i+1 :]
			print "B:", b
			print "C:", c
			d = b + c
			return a + permute(d)

def includeMembers(L):
	if not L:
		return L
	else:
		for i in L[0]:
			includeMembers(L[1:])[-1] += i
		
if __name__ == "__main__":
	print includeMembers(['asdf', 'jkl;'])