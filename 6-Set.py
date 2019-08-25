#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sets : Sets are unordered collection of unique elements. 
Meaning there can be only one reprentative of the same object.
"""
t = ()          ## tuples 
s = set()       ## set
print(type(s))
s.add(1)
s.add(2)
print(s)        # {1, 2}

l = [1,2,3,4,1,2,6,5,7]
x = set(l)
print(x)    # {1, 2, 3, 4, 5, 6, 7}
