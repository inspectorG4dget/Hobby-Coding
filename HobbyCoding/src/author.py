'''
Created on Nov 1, 2010

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