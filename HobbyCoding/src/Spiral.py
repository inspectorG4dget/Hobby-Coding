'''
Created on Jan 21, 2012

@author: ashwin
'''


def spiral(n, pad=0):
	x, y = 0, 0
	
	if n <= 0:
		return None
	
	while x < n:
		print x+pad, y+pad
		x += 1

	x -= 1
	y += 1
	while y < n:
		print x+pad, y+pad
		y += 1
	
	x -= 1
	y -= 1
	while x >= 0:
		print x+pad, y+pad
		x -= 1
	
	x += 1
	y -= 1
	while y > 0:
		print x+pad, y+pad
		y -= 1
	
	return spiral(n-2, pad+1)

if __name__ == "__main__":
	spiral(3)