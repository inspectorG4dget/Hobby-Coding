'''
Created on Sep 25, 2010

@author: ashwin
'''

def convert(grade):
	"""Convert a percentage grade into a point on the 4 point GPA system"""
	if grade >= 85: 	return 4.0
	elif grade >= 80:	return 3.7
	elif grade >= 77:	return 3.3
	elif grade >= 73:	return 3.0
	elif grade >= 70:	return 2.7
	elif grade >= 67:	return 2.3
	elif grade >= 63:	return 2.0
	elif grade >= 60:	return 1.7
	elif grade >= 57:	return 1.3
	elif grade >= 53:	return 1.0
	elif grade >= 50:	return 0.7
	else:				return 0.0
	
def cgpa(grades):
	return sum([convert(grade) for grade in grades]) / len(grades)
	
if __name__ == '__main__':
	with open('/home/scripts/grades', 'r') as infile:
		grades = [int(line.split()[1].strip()) for line in infile]
		print "CGPA is:", cgpa(grades)