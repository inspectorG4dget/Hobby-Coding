'''
Created on Nov 1, 2011

@author: ashwin
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
