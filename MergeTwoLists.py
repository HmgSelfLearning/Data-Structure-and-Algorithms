# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 20:58:22 2025

@author: hadis
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        i , j = 0 , 0
        merged = []
        while i < len(list1) and j < len(list2):
            if list1[i]<list2[j]:
                merged.append(list1[i])
                i+=1
            else:
                merged.append(list2[j])
                j+=1

        while i<len(list1):
            merged.append(list1[i])
            i+=1

        while j<len(list2):
            merged.append(list2[j])
            j+=1   

        return merged
    
    
nums1 = [1, 2, 4]
nums2 = [1, 3, 4]
sol = Solution()
print(sol.mergeTwoLists(nums1, nums2))    