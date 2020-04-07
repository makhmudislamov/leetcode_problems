"""
Write a function fib() that takes an integer nn and returns the nnth Fibonacci ↴ number.

Let's say our Fibonacci series is 0-indexed and starts with 0. So:

  fib(0)  # => 0
fib(1)  # => 1
fib(2)  # => 1
fib(3)  # => 2
fib(4)  # => 3
...
"""

import unittest

# BOTTOM UP - TIME AND SPACE - O(n) and O(1)
def fib(n):
    if n < 0:
        raise Exception("Negative Input")

    if n in [0, 1]:
        return n

    # tracking previous 2 numbers for bottom up
    prev_prev = 0
    prev = 1

    for _ in range(n-1):
        current = prev + prev_prev # calculating next fib
        # moving the trackers to next two numbers
        prev_prev = prev
        prev = current

    return current



# MEMOIZATION - Time and Space  - O(n)
# class Fibonacci(object):
#     def __init__(self):
#         self.memo = {}


# def fib(n):
#     memo = {}
#     if n < 0 :
#         raise Exception("Negative Input")

#     if n in [0,1]:
#         return n
    # if we already calculated for n
    # if n in memo:
    #     return memo[n]
    
    # result = fib(n-1) + fib(n-2)
    # memo[n] = result

    # return result

# RECURSIVE - exponential - NOT GOOD
# def fib(n):
    # TIME and SPACE COMPLEXITY: O(2**n)  - exponential
    # if n in [0,1]:
    #     return n
    # return fib(n-1) + fib(n-2)


    # Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)
