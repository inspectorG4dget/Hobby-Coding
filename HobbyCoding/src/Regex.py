'''
Created on Sep 15, 2011

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

from re import search

#text = open('regexDoc', 'r').read()
#regex = '([Rr]eg){1}(ular ?|([Ee]xpressions?|[Ee]x(p|es)))'

#text = 'purple alice-b@@google.com monkey dishwasher'
text = 'purple alice-b@@google.com monkey dishwasher'
regex = r'[\w]+-*[\w.]+@@[\w.-]+[(com)(co\. .{2})]'

#text = 'purple alice-b@@google.com monkey dishwasher'
#regex = r'.+-*[\w.]+@@[\w.-]+'

match = search(regex, text)
print match.group()