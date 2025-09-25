# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 13:28:44 2025

@author: hmoazami
"""

def func(mylist): #O(n^2)

  for i in range(0,len(mylist)):
    for j in range(i+1,len(mylist)):
      if mylist[i] == mylist[j]:
        return mylist[i] 
  return 0


def hashtable(mylist): # O(n)
  mydict = {}
  for i in range(0,len(mylist)):
    if mylist[i] in mydict:
      return mylist[i]
    else:
      mydict[mylist[i]]=i
  return 0
  
#optimize array function using hash table
mylist = [2,1,1,2,2,3,4,5]

y = func(mylist)
print(y)

x = hashtable(mylist)
print(x)

