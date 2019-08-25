#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
r   - read
w   - write
w+  - open write and read
a   - append
"""

#""" ## Witing over the file
f = open('textfile.txt','w+')
f.write("First Line\n")
f.write("Second Line\n")
f.write("I'm Reading something into file")
f.close()
"""

## Reading from the file
f = open('textfile.txt','r')
print(f.read())
#print(f.readlines())    ## output as list format
#f.seek(50)              ## reset the "cursor" for reading text  
#print(f.read())
f.close()
#"""

for lines in open('textfile.txt'):
    print(lines)