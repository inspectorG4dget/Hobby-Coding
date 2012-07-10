'''
Created on Sep 24, 2010

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

#sequence = "a t c t g g t c c t g g c c c a a a t t a"

class Range:
	def __init__(self, start, end):
		self.setStart(start)
		self.setEnd(end)
		
	def getStart(self):
		return self.start
	
	def setStart(self, s):
		self.start = s
		
	def getEnd(self):
		return self.end
	
	def setEnd(self, e):
		self.end = e
		
	def getLength(self):
		return len(range(self.start, self.end))
	
	def overlaps(self, r):
		if 	(r.getStart() < self.getEnd() and r.getEnd() >= self.getEnd()) or \
			(self.getStart() < r.getEnd() and self.getEnd() >= r.getEnd()) or\
			(self.getStart() >= r.getStart() and self.getEnd() <= r.getEnd()) or \
			(r.getStart() >= self.getStart() and r.getEnd() <= self.getEnd()):
			return True
		else:
			return False
	
def testOverlap(lst):
	aStart, aEnd = lst[0]
	bStart, bEnd = lst[1]
	
	A = Range(aStart, aEnd)
	B = Range(bStart, bEnd)
	
	return A.overlaps(B)

class DNAFeature(Range):
	
	def __init__(self, start, end):
		self.setStart(start)
		self.setEnd(end)
		self.strand = None
		self.sequencename = None
	
	def setStrand(self, s):
		self.strand = s
		
	def getStrand(self):
		if self.sequenceName == 'plus':
			return 1
		elif self.sequenceName == 'minus':
			return -1
		else:
			return 0
		
	def setSequenceName(self, s):
		self.sequencename = s
		
	def getSequenceName(self, s):
		return self.sequenceName

class GenoModel(DNAFeature):
	
	def __init__(self, start, end):
		self.setStart(start)
		self.setEnd(end)
		self.strand = None
		self.sequencename = None
		self.exons = []
		self.translStart = None
		self.translStop = None
		self.displayId = None
	
	def getFeats(self):
		self.exons.sort(cmp=self.start)
		return self.exons
	
	def addFeat(self, f):
		
		if type(f) == DNAFeature:
			self.exons.append(f)
		else:
			raise TypeError("Cannot add feature as it is not of type DNAFeature")
		
	def setTranslStart(self, i):
		
		if type(i) != int:
			raise TypeError("Cannot set translStart as it is not of type int")
		elif i < 0:
			raise ValueError("Cannot set tanslStart to a negative int")
		else:
			self.translStart = i
		
	def getTranslStart(self):
		return self.translStart
	
	def setTranslStop(self, i):
		
		if type(i) != int:
			raise TypeError("Cannot set translStop as it is not of type int")
		elif i <= 0:
			raise ValueError("Cannot set tanslStop to anything less than 1")
		else:
			self.translStop = i
		
	def getTranslStop(self):
		return self.translStop
	
	def setDisplayId(self, s):
		
		if type(s) != str:
			raise TypeError("Cannot set desiplayId as it is not of type string")
		else:
			self.displayId = s
	
	def getDisplayId(self):
		return self.displayId
	
if __name__ == "__main__":
#	print testOverlap([[1, 5], [5, 10]])
	print 'starting'
	A = Range(1,7)
	print A
