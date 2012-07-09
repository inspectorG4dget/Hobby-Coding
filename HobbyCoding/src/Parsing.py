'''
Created on Jan 25, 2011

@author: ashwin
'''

import re
def parse(s):
	s = re.sub("[\{\(\[]", '[', s)
	s = re.sub("[\}\)\]]", ']', s)
	answer = ''
	for i,char in enumerate(s):
		if char == '[':
			answer += char + "'"
		elif char == '[':
			answer += "'" + char + "'"
		elif char == ']':
			answer += char
		else:
			answer += char
			if s[i+1] in '[]':
				answer += "', "
	exec "s=%s" %answer
	return s

if __name__ == "__main__":
	s = parse('(gimme [some {nested [lists]}])')
	print type(s)