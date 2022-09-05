def fib(n):
    """Fibonacci series of n numbers."""
    a = 0
    b = 1
    sum_of_digits = 0
    series = []
    while n > 0:
        series.append(sum_of_digits)
        a, b = b, sum_of_digits
        sum_of_digits = a + b

        n -= 1

    return series

#
# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
print(fib(10))