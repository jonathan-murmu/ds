'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # length = len(s)
        # for i in range( length//2 ):
        #     temp = s[i]
        #     s[i] = s[(length-1) - i]
        #     s[(length - 1) - i] = temp
        #
        #     # s[i], s[(length - 1) - i] = s[(length - 1) - i], s[i]

        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return s


s = ["h","e","l","l","o"]
# s = ["H","a","n","n","a","h"]

obj = Solution()
print(obj.reverseString(s))