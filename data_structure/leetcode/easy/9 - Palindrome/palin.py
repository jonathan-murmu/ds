class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)

        idx_1 = 0
        idx_2 = len(string) - 1

        while idx_1 < idx_2:
            if string[idx_1] != string[idx_2]:
                return False

            idx_1 += 1
            idx_2 -= 1

        return True
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x > 0 and x%10 == 0):   
#             return False

#         rev = 0

#         while x>rev:
#             rev = rev * 10 + x%10
#             x = x // 10

#         if rev == x or rev//10 == x:
#             return True
#         else:
#             return False

