"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set prev to None
        prev = None

        # iterate till last
        while head:
            # set cur to head, i.e. move cur one step
            cur = head
            # move head to next node, i.e. move head one step
            head = head.next  # now head and cur both point to next node

            # update cur to point to prev
            cur.next = prev

            # move prev to next node, i.e. move prev one step.
            prev = cur

        return prev

