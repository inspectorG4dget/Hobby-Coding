'''
Created on Mar 16, 2012

@author: ashwin
'''

from copy import deepcopy as clone
from inspect import getargspec as spec
from random import randint, choice as choose
from population import *
from settings import *
from crossover import getCrossPoint, getHeight, crossover

def pointMutation(indiv, F, T):
	M = getCrossPoint(indiv)
	iparent,isubtree = None, indiv
	i = [0] if not M else M
	
	while i:
		iparent = isubtree
		isubtree = isubtree.operands[i.pop(0)]
		
	if hasattr(isubtree.operator, "__call__"):
		arity = len(spec(isubtree.operator))
		otherGuys = [f for f in F if len(spec(f)) == arity and f!=isubtree.operator]
		isubtree.operator = choose(otherGuys)
	else:
		otherGuys = [t for t in T if t!=isubtree.operator]
		isubtree.operator = choose(otherGuys)
	
	return [indiv]
		

def headlessChickenMut(indiv, SCORES, F, T, scorefunc, scoreparams, maxheight):
	from population import Node, generateFull, generateGrow, functify
	height = getHeight(indiv)
	chicken, rooster = generateFull(F, T, Node(), height), generateGrow(F, T, Node(), height, maxheight)

	c1, c2 = crossover(indiv, chicken, maxheight)
	c3, c4 = crossover(indiv, rooster, maxheight)
	c5, c6 = crossover(chicken, rooster, maxheight)
	
	for c in [c1, c2, c3, c4, c5, c6]:
		if functify(c) not in SCORES:
			SCORES[functify(c)] = scorefunc(c, *scoreparams)
	
	return sorted([c1, c2, c3, c4, c5, c6], key=lambda f: SCORES[functify(c)], reverse=True)

#if __name__ == "__main__":
#	print 'starting'
#	
#	from cPickle import load
#	n = load(open('testbed'))
#	
#	print GCP(n,7)
#	
#	print 'done'