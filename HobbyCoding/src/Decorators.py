'''
Created on Aug 26, 2011

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

@myDecorator
@someDec
def add(a, b):
	print 'add'
	return a+b
	
if __name__ == "__main__":
	print add(3, 5)