'''
Created on Aug 1, 2011

@author: ashwin

 Licensed to Ashwin Panchapakesan under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 Ashwin licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
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