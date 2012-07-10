'''
Created on Nov 13, 2011

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

def add(s, t):	# this is the first attempt. Most versatile code, but not the most elegant code
	answer = 0
	try:
		n = s.next()	# is this checked? What happens if input is empty stream
	except:
		answer = 0
		for i in t:
			answer *= 10
			answer += i
		
		return answer
	else:
		while n:
			try: m = t.next()
			except: m = 0	# interesting hack. Can be solved in other ways, too
			
			sum = m+n
			if sum/10:
				answer += 1
			answer *= 10
			answer += sum%10
			try: n = s.next()
			except: n = 0
		
		try: m = t.next()	# checking for end of stream
		except: return answer
		else:
			while m:
				answer *= 10
				answer += m
				try: m = t.next()
				except: return answer

def addEqual(s, t):
	answer = 0
	try: n = s.next()
	except: return answer
	
	while 1:
		m = t.next()
		answer += (m+n)/10	# adding any carry. Works even if there is no carry
		answer *= 10	# horner's rule
		answer += (m+n)%10	# this is beautiful as it works both when there is a carry and when there isn't one
		
		try: n = s.next()
		except: return answer
		
def addUnequal(s, t):
	answer = 0
	try: n = s.next()
	except:
		try: m = t.next()
		except: n = 0
		while 1:
			answer += (m+n)/10
			answer *= 10
			answer += (m+n)%10
			
			try: m = t.next()
			except: return answer
	
	else:
		while 1:
			try: m = t.next()
			except: m = 0
			answer += (m+n)/10
			answer *= 10
			answer += (m+n)%10
			
			try: n = s.next()
			except: 
				try: m = t.next()
				except: return answer
		
def generateNum(n):
	for i in xrange(n, 0, -1):
		yield i

if __name__ == "__main__":
	print 'starting'
	print addUnequal(generateNum(4), generateNum(4))