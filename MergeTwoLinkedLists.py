# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 21:11:43 2025

@author: hadis
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next            
    
    
# Manually create two linked lists:
# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# list1: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# list2: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge them
sol = Solution()
merged = sol.mergeTwoLists(list1, list2)  

# Print merged linked list
print("Merged linked list:")
while merged:
    print(merged.val, end=" ")
    merged = merged.next