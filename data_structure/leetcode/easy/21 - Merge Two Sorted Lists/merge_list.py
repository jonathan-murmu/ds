"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # initialize head = cur = Blank Node
        head = cur = ListNode()

        # iterate until any one is None
        while list1 and list2:
            # compare list1 and list2 values
            if list1.val <= list2.val:
                # cur.next = smaller
                cur.next = list1
                list1, cur = list1.next, list1
                # cur = list1
                # list1 = list1.next
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                # cur = list2
                # list2 = list2.next

        # if any lists are still left
        if list1 or list2:
            cur.next = list1 if list1 else list2
            # if list1:
            #     cur.next = list1
            # else:
            #     cur.next = list2

        return head.next


def create_linked_list(arr):
    next = None
    list = []
    for i in arr:
        next = ListNode(i, next)
        list.append(next)

    return list

obj = Solution()
list1 = [2,4,5,6,8]
list2 =  [1,3,5]
obj.mergeTwoLists(list1, list2)

