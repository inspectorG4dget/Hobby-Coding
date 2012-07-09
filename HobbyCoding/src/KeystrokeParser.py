'''
Created on Feb 2, 2011

@author: ashwin
'''

def shift(s):
	LOWER = '`1234567890-=[];\'\,./'
	UPPER = '~!@@#$%^&*()_+{}:"|<>?'
	
	if s.isalpha():
		return s.upper()
	else:
		return UPPER[LOWER.index(s)]

def parse(input):
	input = input.split("[BACKSPACE]")
	answer = ''
	i = 0
	while i<len(input):
		s = input[i]
		if not s:
			pass
		elif i+1<len(input) and not input[i+1]:
			s = s[:-1]
		else:
			answer += s
			i += 1
			continue
		answer += s[:-1]
		i += 1
		
	return ''.join(shift(i[0])+i[1:] for i in answer.split("[SHIFT]") if i)

if __name__ == "__main__":
	print parse("[SHIFT]this isrd[BACKSPACE][BACKSPACE] an example file[SHIFT]1")