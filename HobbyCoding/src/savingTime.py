author: ashwin
'''

def printTime(h, m):
	face = {
			0: "        o",             \
			1: "    o       o",         \
			2: " o             o",     \
			3: "o               o",    \
			4: " o             o",     \
			5: "    o       o",         \
			6: "        o",         \
			}
	h %= 12
	m /= 5

	if 0 <= h <= 6:
		face[h] = face[h][:-1] + 'h'
	else:
		face[12-h] = face[12-h].replace('o', 'h', 1)

	if 0 <= m <= 6:
		temp = list(face[m])
		temp[-1] = 'x' if temp[-1] == 'h' else 'm'
		face[m] = ''.join(temp)
		
	else:
		temp = list(face[12-m])
		i = [i for i in range(len(temp)) if temp[i]!=' '][0]
		temp[i] = 'x' if temp[i]=='h' else 'm'
		face[12-m] = ''.join(temp)

	print '\n\n'.join(face.values())

def run(digitime):
	h, m = digitime.split(':')
	printTime(int(h), int(m))

if __name__ == "__main__":
	import sys
	run(sys.stdin.realine().strip())