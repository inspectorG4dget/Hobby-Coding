'''
Created on Jun 24, 2012

@author: ashwin
'''

from copy import deepcopy as clone
from inspect import getargspec as spec
from random import randint

def countNodes(root, sum=0):
	if not hasattr(root, "operands"):
		return sum+1
	else:
		for i in xrange(len(spec(root.operation))):
			sum += countNodes(root.operands[i], sum+1)
		return sum
	
def getHeight(root, height=0):
	if not hasattr(root.operator, "__call__"):
		return height
	else:
		return max((getHeight(E, height+1) for E in root.operands))
#		return min(map(lambda E: getHeight(E, height+1), root.operands))

def getSize(root):
	if not hasattr(root.operator, "__call__"):
		return 1
	else:
		answer = 1
		for E in root.operands:
			answer += getSize(E)
	
		return answer

def getCrossPoint(root, r=None, id=None):
	
	if r is None: r = randint(1, getSize(root)) % getSize(root)
	if id is None: id = []
	
	if not hasattr(root.operator, '__call__'):
		return id
	
	sizes = zip(root.operands, map(getSize, root.operands))
#	sizes.sort(key=lambda (_,size): size)
	for i,e in enumerate(sizes):
		if r < sum((z[1] for z in sizes[:i+1])):
			return getCrossPoint(e[0], r, id+[i])
		elif r > sum((z[1] for z in sizes[:i+1])):
			try: 
				sizes[i+1][0]
				return getCrossPoint(sizes[i+1][0], r-sum((z[1] for z in sizes[:i+1]))+1, id+[i+1])
			except: 
				return id
		else:
			return id+[0]

def crossover(p1, p2, maxHeight):
	from population import functify
#	print functify(p1)	##
#	print functify(p2)	##
	orig = map(clone, [p1,p2])

	if (getHeight(p1) >= maxHeight) and (getHeight(p2) >= maxHeight): return orig

	_=True
	attempts = 0
	while (getHeight(p1) > maxHeight) or (getHeight(p2) > maxHeight) or _:
#		print 'attempt', attempts	##
#		print 'while'	##
		_=False
		attempts += 1
		if attempts > 5: return p1,p2
		
		p1,p2 = map(clone, [p1,p2])
		I,J = map(lambda r: getCrossPoint(r), [p1,p2])
		I,J = map(lambda L: [0] if not L else L, [I,J])
		i,j = I[:], J[:]
		
		iparent,isubtree = None, p1
#		print 'i:', functify(isubtree)	##
#		print '\t', i	##
		while i:
			iparent = isubtree
			isubtree = isubtree.operands[i.pop(0)]
		
		jparent,jsubtree = None, p2
#		print 'j:', functify(jsubtree)	##
#		print '\t', j	##
		while j:
			jparent = jsubtree
			jsubtree = jsubtree.operands[j.pop(0)]
			
	iparent.operands[I[-1]], jparent.operands[J[-1]] = jsubtree, isubtree
	
#	print 'returning'	##
	return p1,p2