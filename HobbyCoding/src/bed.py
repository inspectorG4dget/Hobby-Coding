'''
Created on Oct 17, 2010

@author: ashwin
'''

import cPickle

def readBed(filepath):
	with open(filepath, 'r') as f:
		data = cPickle.load(f)
		return data
	
def writeBed(models, filepath):
	with open(filepath, 'w') as f:
		cPickle.dump(models, f)