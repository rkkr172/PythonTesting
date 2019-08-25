#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:59:10 2019
@author: root
1.) Creating Strings
2.) Printing Strings
3.) String Indexing and Slicing
4.) String Properties
5.) String Methods
6.) Print Formatting
https://docs.python.org/3/reference/lexical_analysis.html#f-strings
"""

s = 'Hello'
"""
print(s[1:3])
print(s[:-1])
print(s[::-1])
print(s*3)    #Repeatation
#for i in s: print(i);
"""

s1 = ' This is a simple textline'
# upper, lower, capitalize, len, split, find
"""  
print(s1[2::])
print(s1[::-1])
print(len(s1))

a = s + s1
b = a.split()
print(s1.split('i'))
print(a)
print(a.find('i'))

# Formatting
print("He said, my name is %s "%'ROHIT')    # printing simple input
print("He said, my name is %r "%'ROHIT')    # printing Quational input
print("String is %s"%3.45)          # Strint printing
print("Integer is %d"%3.45)         # Integer printing
print("Float is %.2f "%3)           # float printing 2 decimal step
print(f'{s} \t How Are \n you ?')   # tab (\t), next line(\n)
print("The {2} {1} {0}".format('Fox','Brown','Quick'))

print("{0:<9} | {1:^9} | {2:>9}".format('left','center','right'))
print("{0:<9} | {1:^9} | {2:>9}".format('11','22','33'))
print("{0:=<9} | {1:-^9} | {2:.>9}".format('11','22','33'))
"""
num = 23.45
#Float formatting follows 
#"result: {value:{width}.{precision}}"
#"{value:10.4f}"
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{4}}")