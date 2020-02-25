"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
"""
class Solution:
    def reverseString(self, s, i=0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # set two pointers from the end and the beginning of the arr
        # swap the items in the pointers and 
        # move the pointers towards each other

        # start = 0
        # end = len(s) - 1
        # print(s)
        # while start <= end:
        #     s[start], s[end] = s[end], s[start]
        #     start += 1
        #     end -= 1
        # print(s)

        # RECURSIVE , additinal argument i=0
        if i < len(s) // 2:
            s[i], s[-i-1] = s[-i-1], s[i]
            print("0", s[0])
            print("-i-1",s[-i-1])

            self.reverseString(s, i + 1)



sol = Solution()
print(sol.reverseString(["h", "e", "l", "l", "o"]))
# print(sol.reverseString(["H", "a", "n", "n", "a", "h"]))
