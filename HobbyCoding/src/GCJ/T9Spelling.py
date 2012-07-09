'''
Created on May 19, 2011

@author: ashwin
'''

def sms(msg):
	answer = ''
	mapping = {'a':'2',
	'b':'22',
	'c':'222',
	'd':'3',
	'e':'33',
	'f':'333',
	'g':'4',
	'h':'44',
	'i':'444',
	'j':'5',
	'k':'55',
	'l':'555',
	'm':'6',
	'n':'66',
	'o':'666',
	'p':'7',
	'q':'77',
	'r':'777',
	's':'7777',
	't':'8',
	'u':'88',
	'v':'888',
	'w':'9',
	'x':'99',
	'y':'999',
	'z':'9999',
	' ':'0'
	}
	
	for char in msg:
		key = mapping[char]
		if answer.endswith(key[0]):
			answer += ' '
		answer += key
	return answer

def run(infilepath, outfilepath):
	infile = open(infilepath, 'r')
	outfile = open(outfilepath, 'w')
	
	for case in xrange(1, int(infile.readline().strip())+1):
		outfile.write("Case #%d: %s\n" %(case, sms(infile.readline().rstrip('\n'))) )
		
	
if __name__ =="__main__":
	print 'starting'
	infilepath = 'C-large-practice.in'
	outfilepath = 'C-large-practice.out'
	run(infilepath, outfilepath)
	print 'done'