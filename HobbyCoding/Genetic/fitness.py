'''
Created on Jun 24, 2012

@author: ashwin
'''

from itertools import izip

from individual import functify

def myround(n, base):
	return int(base * round(float(n)/base))

def score(func, inputs, targets):
	""" fitness function. Counts number of hits, normalized to a scale of 1"""
#	print 'precision:', precision	##
	precision = 3
	if type(func) != type(''): func = functify(func)
	score = 0.0
	for input, target in izip(inputs, targets):
		evalfunc = func[:]
		for i in xrange(1, len(input)+1):
			evalfunc = evalfunc.replace("x%s"%i, str(input[i-1]))
#			print evalfunc	##
		
		try:
			val = round(eval(evalfunc), precision)
#			print 'val:', val; #crash()
#			print 'target:', target; #crash()
#			score -= val!=round(target, precision)
			score -= (val-round(target, precision))**2
#			print 'score:', score; crash()	##
		except:
#			print 'excepted'; raise	##
			score -= 30000	#arbitrarily large number

	return score#/len(inputs)