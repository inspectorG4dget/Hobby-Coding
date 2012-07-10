'''
Created on Sep 22, 2010

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