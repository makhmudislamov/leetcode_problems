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

        start = 0
        end = len(s) - 1
        print(s)
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        print(s)

        # RECURSIVE , additinal argument i=0
        # if i < len(s) // 2:
        #     s[i], s[-i-1] = s[-i-1], s[i]
        #     print("0", s[0])
        #     print("-i-1",s[-i-1])

        #     self.reverseString(s, i + 1)



sol = Solution()
# print(sol.reverseString(["h", "e", "l", "l", "o"]))
print(sol.reverseString(["T"," ","0","j","y"," ","X","3","8","0","L","m","l","E","J","."," ",";","Q","v","4","`","c","l","?","u","g",",","t"," ","8"," ","\"","!","H","I","J","E","M","H","`","R","L","J","\"","f",";","z"," ","6",";","u","I","?","C","6","I","`","R","H","\"","8","n",":","5","Z","8",";","b","I",",","'","d","!",",","2","k","a","\"","'","6","?","`","8","'","y","r",",",",",":","E","F","i"," ",",","G"," "," ","6","7","?","G","8","k","J",",","2","X","Y","b","i","W","W","w","o","i","!","0","\"","O",",","2","Q"," ","t","b","n"," ","9","B"," ","x","\"","F","a","F","W",","," ","p","!",";","'","F","I","6","9","Z","3","C","b","b","X","n","V","1","x","P","'","`","?","F","'","m","\"",".","e","5","?",":","c","F","`","\"",",","u","k","4","O"," ","W",";"," ","1",":","0"," ",":","o",";","b",",","Q",",","b",";","o",":"," ","0",":","1"," ",";","W"," ","O","4","k","u",",","\"","`","F","c",":","?","5","e",".","\"","m","'","F","?","`","'","P","x","1","V","n","X","b","b","C","3","Z","9","6","I","F","'",";","!","p"," ",",","W","F","a","F","\"","x"," ","B","9"," ","n","b","t"," ","Q","2",",","O","\"","0","!","i","o","w","W","W","i","b","Y","X","2",",","J","k","8","G","?","7","6"," "," ","G",","," ","i","F","E",":",",",",","r","y","'","8","`","?","6","'","\"","a","k","2",",","!","d","'",",","I","b",";","8","Z","5",":","n","8","\"","H","R","`","I","6","C","?","I","u",";","6"," ","z",";","f","\"","J","L","R","`","H","M","E","J","I","H","!","\""," ","8"," ","t",",","g","u","?","l","c","`","4","v","Q",";"," ",".","J","E","l","m","L","0","8","3","X"," ","y","j","0"," ","T"]))
# print(sol.reverseString(["H", "a", "n", "n", "a", "h"]))
