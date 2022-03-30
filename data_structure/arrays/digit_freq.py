'''Digit frequency

Given a single digit k find out how many times it appears in the given number n.
'''

def digit_freq(n, k):
    count = 0
    while n > 0:

        if ((n % 10) == k):
            count += 1

        n = n//10

    return count


count = digit_freq(99823739, 3)

print(count)
