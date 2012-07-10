'''
Created on May 5, 2012

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

from itertools import count
import easygui as eg
from datetime import date as DATE, datetime as DT

class Event:
	ID = count()
	def __init__(self, date, time, message, preconditions, nexts, status=False):
		if date and type(date) != DATE: raise TypeError("date parameter has to be of type datetime.date")
		if time and type(time) != DT: raise TypeError("time parameter has to be of type datetime.datetime")
		
		if type(preconditions) != set: preconditions = {p for p in preconditions}
		if type(nexts) != set: nexts = {n for n in nexts}

		self.id = self.ID.next()
		self.date = date
		self.time = time
		self.message = message
		self.preconditions = preconditions
		self.next = nexts
		self.status = status
	
	def __repr__(self):
		return str(self.id)
	
	def __str__(self):
		return "%s: %s, %s -> %s" %(self.id, self.date, self.time, self.message)
	