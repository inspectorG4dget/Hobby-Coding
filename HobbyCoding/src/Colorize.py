'''
Created on Aug 1, 2011

@author: ashwin
'''

import Image

def blue_to_red(infilepath):
	pic = Image.open(infilepath)
	width, height = pic.size
	for x in xrange(width):
		for y in xrange(height):
			r, g, b = pic.getpixel((x,y))
			if b > 128:
				b = 0
				r = max(r+b, 255)
				pic.putpixel((x,y), (r, g, b))
	
	pic.save('/home/ashwin/Desktop/modified.jpg')
		
if __name__ == "__main__":
	print 'starting'
	blue_to_red('/home/ashwin/Desktop/pic.jpg')
	print 'done'