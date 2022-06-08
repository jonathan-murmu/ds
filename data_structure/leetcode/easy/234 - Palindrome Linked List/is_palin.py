"""
https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""



from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        # find mid way(slow) and fast will reach last.
        # reverse the 1st half of the linked list
        while fast and fast.next:
            fast = fast.next.next  # move very fast
            rev, rev.next, slow = slow, rev, slow.next

        if fast:  # for odd nodes
            # move slow one step.
            slow = slow.next

        # rev will move backwards untill None, slow will move forward.
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        # if the above loop stopped before finishing rev(i.e. rev=None)
        # then that means that rev's val and slow's value are not equal
        # so return False(not of non-zero)
        # if the above loop finishes, rev will become None. So retun True (not of None)
        return not rev
