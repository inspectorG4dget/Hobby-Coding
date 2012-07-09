'''
Created on Jan 17, 2011

@author: ashwin
'''
def f(L, length, s=''):
	print s
	if len(s) == length:
		print s
	else:
		for word in L:
			for char in word:
				w = word.replace(char, '')
				l = L[:]
				l.remove(word)
				l.append(w)
				f(l, length, s+char)
				
if __name__ == "__main__":
	L = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '0123456789']
	f(L, 2, '')