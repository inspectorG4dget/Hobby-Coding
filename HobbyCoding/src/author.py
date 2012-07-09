'''
Created on Nov 1, 2010

@author: ashwin
'''


original = "Hooray! Finally, we're done"
seps = "!,"

def splice(original, seps):
	texts = [original]
	for sep in seps:
#		texts = texts[0].split(seps[i])
		temp = []
		for t in texts:
			temp.extend(t.split(sep))
		texts = temp
	print texts
	
if __name__ == "__main__":
	original = "Hooray! Finally, we're done"
	seps = "!,"
	splice(original, seps)