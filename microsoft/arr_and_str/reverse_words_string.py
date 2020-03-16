"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


def reverseWords(s: str) -> str:
    # first clean the input from trailing / in between extra spaces
    # try to use join to save the words in a space
    # iterate the list from backwards and append it to predecalred string
    # print the string 
    # BRUTEFORCE
    # output = ""
    # s = s.split()
 
    # for string in s[::-1]:
    #     if len(string) != 0:
    #         output += string + " "
    # return output.strip()

    # OPTIMIZATION
    return " ".join(reversed(s.split()))
        
            
        
    


# s = "  hello world!  "
s = "a good   example"
print(reverseWords(s))
