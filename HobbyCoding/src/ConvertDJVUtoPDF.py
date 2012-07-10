'''
Created on Sep 19, 2010

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

from os import system as cmd, listdir as ls, chdir as cd

def convertToTIFF():
    for i in ls('.'):
            fname = i.split('.')[0].replace(" ", "\\ ")
            cmd('ddjvu -format=tiff %s.djvu %s_tiff.tiff' %(fname, fname))
            cmd('rm -f "%s"' %i)

def converToPDF():
    for i in (_ for _ in ls('.') if _.endswith(".tiff")):
            fname = i.split('.')[0].replace(" ", "\\ ")
            cmd('tiff2pdf -j -o  "%s.pdf"  "%s_tiff.tiff"' %(fname, fname))
            cmd('rm -f "%s"' %i)

if __name__ == "__main__":
    cd('/home/ashwin/Desktop/Trying/')
    convertToTIFF()
    converToPDF()

