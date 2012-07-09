'''
Created on Sep 19, 2010

/bin/bash: :q: command not found
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

