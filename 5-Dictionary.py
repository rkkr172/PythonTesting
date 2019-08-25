#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1.) Constructing a Dictionary
2.) Accessing objects from a dictionary
3.) Nesting Dictionaries
4.) Basic Dictionary Methods

dict:- Dictionaries are unordered mapping for storing objects. 
Previously we saw how lists store objects in an ordered sequence dictionaries 
use a key-value pairing instead.
This key:- value pair allow users to quickly grab objects without 
needing to know an index location.

#### When to choose dictionary or lists ?
#Dictionary: Objects retrieved by key name. Unordered and can not be sorted.
#Lists: Objects retrieved by location. Ordered sequence can be indexed or sliced.
"""

#1.) Constructing a Dictionary
d = {1:'abc',2:'xyz',3:'apple',4:100}
#"""
print(type(d))
print(d)

print(f"{d[1]} at place d['c']")
print(d[3][1:].upper())

d[4] *= 12
d[1] = 'abcxyz'
print(d)

#3.) Nesting Dictionaries
d1 = {'key1':{'nestkey':{'subnestkey':'value'}}}
print(d1['key1']['nestkey']['subnestkey'])

#4.) Basic Dictionary Methods
#d = {1:'abc',2:'xyz',3:'apple',4:100}
print(d.keys())
print(d.values())
print(d.items())

for i in d:
    #print(i)    #key
    print(d[i]) #value
#"""


