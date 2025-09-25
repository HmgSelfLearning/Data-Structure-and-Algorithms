# -*- coding: utf-8 -*-
"""
Created on Mon May 19 15:50:09 2025

@author: hmoazami
"""

def MaxSub(arr):
    maximum = 0
    summ = []
    
    for i in range(len(arr)):
        all_sum = 0
        
        for j in range(i, len(arr)):    
            all_sum += arr[j]
            summ.append(all_sum)
            maximum = max(all_sum, maximum)

    return maximum, summ


arr = [1,4,2,-1,5]

out = MaxSub(arr)
print(out)