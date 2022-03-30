def isPalindrome( n: int) -> bool:
    temp = n
    rev = 0

    while temp>0:
        digit = temp%10
        rev = rev * 10 + digit
        temp = temp // 10

    if rev == n:
        return True
    else:
        return False

print(isPalindrome(1921))