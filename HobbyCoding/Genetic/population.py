'''
Created on Mar 15, 2012

@author: ashwin
'''

from inspect import getargspec as spec
from random import choice as choose
from itertools import izip
from cPickle import load, dump
from sys import exit as crash
from GP import *
from individual import *

def generateFull(F, T, root, height):
	if height < 0:
		root.operator = choose(T)
		return root
	
	else:
		root.operator = choose(F)
		for _ in spec(root.operator).args:
			n = Node()
			root.operands.append(generateFull(F, T, n, height-1))
	
		return root

def generateGrow(F, T, root, height, minheight):
	if height < 0:
		root.operator = choose(T)
		return root
	
	else:
		if minheight>0: root.operator = choose(F)
		else: root.operator = choose(F+T)
		if hasattr(root.operator, "__call__"):
			for _ in spec(root.operator).args:
				n = Node()
				root.operands.append(generateGrow(F, T, n, height-1, minheight-1))
			return root
		else:
			return root

def generateRamped(F, T, height, N, minheight):
	""" generate N trees of height h for h in range(2,height+1) by each method in [grow, full]"""
	
	return [generateFull(F, T, Node(), height) for _ in xrange(N)] + [generateGrow(F, T, Node(), height, minheight) for _ in xrange(N)]

def genPop(N, height, minheight, genfunc, F, T):
	"""	generate a population of N programs by the method described in genfunc.
		genfunc is either grow, full or ramped"""
	
	answer = []
	if genfunc in [generateFull, generateGrow]:
		answer += genfunc(F, T, Node(), height)
	
	elif genfunc == generateRamped:
		perheight = N/(height-1)	# equal number of programs of each height
		for h in xrange(2, height+1):
			answer += genfunc(F, T, height, perheight/2, minheight)	# half as many programs, each by the full and the grow methods
			
	return answer

#if __name__ == "__main__":
#	print 'starting'
#	
##	f, i, t = load(open('function'))
##	print score(f, i, t)
#	
#	ADFs(); crash()
#	
#	F = [add, subtract, mult, div]
#	T = "x1 x2 x3".split() + [0.0, 1.0, e]
#	
#	f = generateGrow(F, T, Node(), 3)
#	print functify(f)
##	
##	dump((f,i,t), open('function', 'w'))
#	
#	print 'done'
