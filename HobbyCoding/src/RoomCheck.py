'''
Created on Nov 1, 2011

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

import urllib2
rooms={606:'b3112430',628:'b3112434', 631:'b3112437',630:'b3112436',602:'b3112426',603:'b3112428',627:'b3112433',607:'b3112431', 629:'b3112435', 605:'b3112429'}


def getStatus(room):
	response = urllib2.urlopen('http://catalogue.bib.uottawa.ca/html/modal_circ.jsp?item='+rooms[room]+'&language=fr')
	html = response.read()
	if html.rfind('RETOUR')!=-1:		
		temp = html.rpartition('RETOUR ')[2]
		return 'occupied until '+temp.rpartition(' <')[0]
	if html.rfind('EN BIBLIO')!=-1:
		return 'available'

if __name__ == "__main__":
	print '-=Grad Study Rooms Check by Tim=-'
	for i in sorted(rooms):
		print 'room', i, getStatus(i)
