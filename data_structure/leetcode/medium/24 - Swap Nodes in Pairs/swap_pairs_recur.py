"""
https://leetcode.com/problems/swap-nodes-in-pairs/
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:  # head.next = edge case for linked list having 1 element
            return head
        # head already initialised (1st)
        # initialise temp (2nd)
        temp = head.next
        # make recursive call with the 3rd element, i.e. temp.next
        # on return, point 1st element with the recursive group's return value
        head.next = self.swapPairs(temp.next)
        # point 2nd element to 1st.
        temp.next = head
        return temp
