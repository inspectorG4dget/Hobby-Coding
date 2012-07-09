'''
Created on Sep 15, 2011

@author: ashwin
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