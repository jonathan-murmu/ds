class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        self.reverse(i, j, s)

    def reverse(self, i, j, s):
        if i >= j:
            return
        s[i], s[j] = s[j], s[i]
        self.reverse(i + 1, j - 1, s)

