# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 20:22:38 2025

@author: hadis
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                      
nums = [3,2,4]
target = 6          
answer = Solution().twoSum(nums, target)
print(answer)
