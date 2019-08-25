#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    1.) Creating lists
    2.) Indexing and Slicing Lists
    3.) Basic List Methods
    4.) Nesting Lists
    5.) Introduction to List Comprehensions
"""
#l1 = [1,2,3]
#l2 = ['a','b','c']
#l3 = [7,8,9]
#a = l1+l2
"""
for i in l1: print(i);
print(a)
print(a[2:])
print(a[::-2])  #reverse of every 2nd element
print(a[::-1])  #reverse complete of each 1st element

l1[1]=20;           # reassignmnet value
l1.append('A');     # Appending another value
#l1.pop();          # Remove one last value
l1.pop(1)           # remove at index point "1"
print(len(l1))      # length of list
l1.reverse()        # Reverse the list permanent
l1.sort()           # Sort the list
print(l1)
"""

#5.) Introduction to List Comprehensions 
# Allow for a quick construction of list.
matrix = [['a','b','c'],[1,2,3]]
for i in matrix: print(i)
first_col0 = [col[0] for col in matrix]
first_col1 = [col[1] for col in matrix]
print(first_col0)
print(first_col1)

# Matrix
m1 = [['a','b','c'],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        print(f'm1[{i}][{j}] = {m1[i][j]}')
    print("")
    
    
