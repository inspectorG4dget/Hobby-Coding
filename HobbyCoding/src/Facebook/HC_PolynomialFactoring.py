'''
Created on Jan 29, 2011

@author: ashwin
'''

def factor(F, G, H):
	if not F or F==[0]: return H
	elif len(G) > len(F): return "no solution"
	else:
		H.append(float(F[0])/G[0])
		for i in range(1, len(G)):
			F[i] -= G[i]*H[-1]
		return factor(F[1:], G, H)
		
def run(infilepath):
	f = open(infilepath, 'r')
	N = int(f.readline().strip())
	for i in range(N):
		F = [int(i) for i in f.readline().strip().split()][1:]
		G = [int(i) for i in f.readline().strip().split()][1:]
		print factor(F, G, [])
		
	f.close()
	
if __name__ == "__main__":
	run('testin.txt')