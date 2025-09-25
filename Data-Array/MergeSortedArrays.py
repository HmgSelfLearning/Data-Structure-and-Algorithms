# -*- coding: utf-8 -*-
"""
Created on Sun May 18 18:31:19 2025

@author: hadis
"""

def MergSorted(arr1, arr2):
    
    if len(arr1)==0 or len(arr2)==0:
        return arr1+arr2
    
    
    my_list = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            my_list.append(arr1[i])
            i+=1
            
        elif arr1[i]> arr2[j]:
            my_list.append(arr2[j])
            j+=1
            
    return my_list+arr1[i:]+arr2[j:]


arr1 = [1,3,4]

arr2 = []

arr3 = MergSorted(arr1, arr2)
print(arr3)
