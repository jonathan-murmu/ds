def palin(s):
    length = len(s)
    for i in range(length):
        if s[i] != s[(length-1)-i]:
            return False

    return True


print(palin('12321'))

