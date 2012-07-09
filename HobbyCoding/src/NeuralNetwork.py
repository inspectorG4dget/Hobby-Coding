'''
Created on Feb 11, 2011

@author: ashwin
'''

print "     \tFISH\tCHIPS\tBEER"
def learn(wFish, wChips, wBeer):
	print "     \t%f\t%f\t%f" %(wFish, wChips, wBeer)
	actual = 850
	numFish = 2
	numChips = 5
	numBeer = 3
	learning = 1.0/35
	
	weightedSum = (wFish*numFish) + (wChips*numChips) + (wBeer*numBeer)
	error = weightedSum - actual
	
	if not error:
		print "LEARNED"
	else:
		print "DELTA\t%f\t%f\t%f" %(learning*numFish*error, learning*numChips*error, learning*numBeer*error)
		wFish -= (learning*numFish*error)
		wChips -= (learning*numChips*error)
		wBeer -= (learning*numBeer*error)
		print "%f\t%f\t%f" %(wFish, wChips, wBeer)
		learn(wFish, wChips, wBeer)
		
if __name__ == "__main__":
	print "starting"
	learn(50, 50, 50)
	print "done"