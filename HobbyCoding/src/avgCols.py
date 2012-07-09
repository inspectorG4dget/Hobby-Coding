'''
Created on Sep 22, 2010

@author: ashwin
'''
with open('in', "rtU") as f:
	lines = [l for l in f if l.strip()]
	names = '\t'.join(lines[0].split())
	numbers = [[i.strip() for i in line.split()] for line in lines[1:]]
	person_data = zip(*numbers)
	person_data = [tuple(int(i) for i in t if i!="NA") for t in person_data]
	averages = '\t'.join(map(lambda x: str(float(sum(x))/len(x)), person_data ))

with open('out', 'w') as f:
	f.write(names)
	f.write('\n')
	f.write(averages)