'''
Created on Aug 26, 2011

@author: ashwin
'''

class myDecorator:
	def __init__(self, target):
		print "__init__"
		self.func = target
	
	def __call__(self, *args, **kwargs):
		print "__call__"
		if any((type(x)!=int for x in args)):
			raise Exception("Need all ints")
		return self.func(*args, **kwargs)

def someDec(target, *args, **kwargs):
	if any([type(i) != int for i in args]):
		raise Exception("Need all ints")
	else:
		def f(*args, **kwargs):
			return target(*args, **kwargs)
		return f

#@@myDecorator
@@someDec
def add(a, b):
	print 'add'
	return a+b
	
if __name__ == "__main__":
	print add(3, 5)