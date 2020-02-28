"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and 
for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        fizzy_array = []
        num = 1
        while num < n + 1:
            if num % 3 == 0 and num % 5 == 0:
                fizzy_array.append("FizzBuzz")
            elif num % 3 == 0:
                fizzy_array.append("Fizz")
            elif num % 5 == 0:
                fizzy_array.append("Buzz")
            else:
                fizzy_array.append(str(num))
            num += 1

        return fizzy_array

n = 15
s = Solution()
print(s.fizzBuzz(n))
