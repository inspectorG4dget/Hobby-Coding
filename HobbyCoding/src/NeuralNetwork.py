'''
Created on Feb 11, 2011

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