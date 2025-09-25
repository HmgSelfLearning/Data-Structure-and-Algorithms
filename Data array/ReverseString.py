# -*- coding: utf-8 -*-
"""
Created on Sun May 18 16:52:31 2025

@author: hadis
"""
def Reverse(str):
    mylist = []
    for i in range(len(str)-1, -1, -1):
        mylist.append(str[i])
    return ''.join(mylist)

MyStr = Reverse('Hadis is')
print(MyStr)



def reverse2(str):
    return ''.join(reversed(str))

MyStr = reverse2('Hadis is')
print(MyStr)