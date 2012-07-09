'''
Created on Nov 14, 2011

@author: ashwin
'''

from math import sqrt

def hypotenuse(x, y):
	if x>y:
		return x*sqrt((float(y)/x)**2 +1)
	else:
		return y*sqrt((float(x)/y)**2 +1)
	
if __name__ == "__main__":
	print hypotenuse(5,12)