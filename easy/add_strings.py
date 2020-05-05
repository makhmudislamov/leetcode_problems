"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

def addStrings(num1: str, num2: str) -> str:
    # iterate from left both nums
    # convert each s to int
    # add, if sum is > 9, leadin += 1 to next num
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            return str(int(i)+int(j))