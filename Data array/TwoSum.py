# -*- coding: utf-8 -*-
"""
Created on Mon May 19 13:23:42 2025

@author: hmoazami
"""

def TwoSum(nums,target):
    
    remain =[0] * len(nums)
    foundi = -1
    foundj = -1
    
    for i in range(len(nums)):
        remain[i] = target - nums[i]
        j = 0
        
        while j < len(nums):
            if remain[i] == nums[j] and i!=j:
                foundi = i
                foundj = j
                return  [foundi, foundj]
                
            j+=1
            
    print("Not found")    
            
            
                
                
nums = [2,11,7,15]        
target = 9

out = TwoSum(nums, target)
print(out)  

"""
def two_sum(nums, target):
    final_array = []
    obj_indices = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in obj_indices:
            final_array.append(obj_indices[complement])
            final_array.append(i)
        else:
            obj_indices[nums[i]] = i

    return final_array

# Example usage
print(two_sum([3, 2, 4], 6))
"""