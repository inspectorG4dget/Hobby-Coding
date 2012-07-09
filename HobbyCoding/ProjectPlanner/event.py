'''
Created on May 5, 2012

@author: ashwin
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
	