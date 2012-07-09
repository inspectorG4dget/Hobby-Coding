'''
Created on Jun 24, 2012

@author: ashwin
'''

class Individual:
	def __init__(self, chromosomes):
		""" Given a bunch of chromosomes, this individual is a wrapper around them. It holds all chromosomes in place."""
		self.chromosomes = chromosomes

class Node:
	def __init__(self, key=None):
		self.operator = key
		self.operands = []
	
	def __repr__(self):
		if hasattr(self.operator, "__call__"): return self.operator.__name__
		else: return str(self.operator)
	
	def __getitem__(self,i):
		return self.operands[i]

def functify(root):
	if not root.operands:
		o = root.operator
		if hasattr(o, "__call__"): return o.__name__
		else: return str(o)
	else:
		o = root.operator
		if hasattr(o, "__call__"): return "%s(%s)" %(o.__name__, ','.join([functify(r) for r in root.operands]))
		else: return "%s(%s)" %(o, ','.join([functify(r) for r in root.operands]))