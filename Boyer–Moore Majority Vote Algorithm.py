# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 17:33:14 2025

@author: hmoazami
"""


def find_majority_elm(arr):
    candidate = None
    counter = 0
    
    # Step 1: Find the candidate
    for x in arr:
        if counter == 0:
            candidate = x
            counter =1
        elif candidate == x:
            counter +=1
        else:
            counter -= 1
            
    # Step 2: Verify the candidate
    count = sum(1 for x in arr if candidate==x)
    
    if count >= len(arr)//2:
        return candidate
    else: 
        return None
            
# Example usage:
arr = [2, 2, 1, 1, 1, 2, 2, 3, 5, 7, 2, 2]
result = find_majority_elm(arr)

print("Majority element is:", result)            
    
    
    
    
    
    


