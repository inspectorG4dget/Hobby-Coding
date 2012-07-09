'''
Created on Dec 30, 2010

@author: ashwin
'''

def rd(L, w='', answer=[]):
	if not L:
		answer.append(w)
		return answer
	else:
		for char in L[0]:
			rd(L[1:], w+char, answer)

if __name__ == "__main__":
	a = []
	rd(L=['ab', 'cd', 'ef'], answer=a)
	for i in a:
		print i