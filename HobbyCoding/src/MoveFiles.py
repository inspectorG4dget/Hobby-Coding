'''
Created on Aug 1, 2011

@author: ashwin
'''

from shutil import move as mv
from os import walk
from os.path import join as pathjoin

filepaths = set([])

def move(srcs, dest):
	"""Move all the files in srcs to the destination folder dest"""
	
	for src in srcs:
		mv(src, dest)
		
def generateFilenames(root):
	for base, dirs, files in walk(root):
		filepaths.update([pathjoin(base, f) for f in files])
		for dir in dirs:
			generateFilenames(pathjoin(base, dir))
			
if __name__ == "__main__":
	print 'starting'
	generateFilenames("/home/ashwin/Calibre Library/Unknown")
	print filepaths
#	move(filter(lambda x: x.endswith('pdf'), filepaths), '/home/ashwin/SOBooks')
	print 'done'