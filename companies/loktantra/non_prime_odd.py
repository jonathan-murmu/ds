# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


# print non-prime odd numbers between 1-100
# Expected Answer: 9, 15, 21, 25, 27, 33, 35, 39, 45, 49, 51, 55, 57, 63, 65, 69, 75, 77, 81, 85, 87, 91, 93, 95, 99

class Calculate():

    def is_odd(self, num):
        """Check if odd.
        args:
            num (int) - number to check if odd or not.
        returns: boolean
        """
        # TODO: check the type, only except int values.
        return num % 2 != 0

    def is_prime(self, num):
        """Check if prime. Time Complexity O(sqrt(n))
        args:
            num (int) - number to check if odd or not.
        returns: boolean
        """
        # prime numbers are greater than one
        if num <= 1:
            return False

        # iterate from 2 to square of the given number.
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    def is_prime_optimised(self, num):
        """Check if prime. Time Complexity O(sqrt(n)).
        Optimized version, added a few additional checks to reduce the number of iterations,
        but time complexity remains same.
        args:
            num (int) - number to check if odd or not.
        returns: boolean"""

        # prime numbers are greater than one
        if num <= 1:
            return False

        if num == 2 or num == 3:  # Numbers 2 and 3 are prime
            return True

        if num % 2 == 0 or num % 3 == 0:  # Numbers divisible by 2 or 3 are not prime
            return False

        i = 5
        while i * i <= num:  # Iterate until square(i * i) exceeds the given number

            # Check divisibility by i and i + 2, for e.g i=5, then num should not be divisible by 5(i) and 7(i+2)
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6  # Increment i by 6 for skipping multiples of 2 and 3

        # If none of the above conditions matched, the number is prime
        return True

    def display(self, num):
        """Console ouput to display the result."""
        print(num)

    def is_non_prime_odd(self):
        """List all non-prime odd numbers between 1-100."""

        # iterate or 1 to 100 and check for non-prime odd numbers.
        for num in range(2, 101):
            if not self.is_odd(num):
                continue  # continue to next iteration if even numbers.

            if self.is_prime_optimised(num):
                continue  # continue to next iteration if prime number.

            self.display(num)


obj = Calculate()
obj.is_non_prime_odd()











