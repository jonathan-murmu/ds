"""Reverse an string"""
def reverse(string):
    n = len(string)
    result = [""] * n
    for i in range((n+1)//2):
        result[i], result[n-i-1] = string[n-i-1], string[i]
    print(result)

reverse("abcd")