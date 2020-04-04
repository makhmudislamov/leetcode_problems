"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


def reverse( x: int) -> int:
    if -2**31 >= x or x >= 2**31 - 1:
        return 0
    if x > 0:
        x = str(x)
        x = int(x[::-1])
    else:
        x = str(abs(x))
        x = -int(x[::-1])
    print(x)
    if -2**31 >= x or x >= 2**31 - 1:
        return 0
    return x
