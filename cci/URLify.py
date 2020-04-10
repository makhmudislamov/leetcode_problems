"""
Chapter1, page 90
replace all spaces in string with %20
example
input: "John Smith"
output: "John%20Smith"
"""

# questions to ask:
# acceptable and optimal time and space
# !YOU CANNOT MODIFY STRING - STRINGS ARE IMMUTABLE
# modifying the input? ASCII?

# approach 1 - time and space >> O(n) and O(n)
# iterate over the string if the char is " " replace it with %20

def urlify(s):
    # base cases
    if not s:
        return s
    if s == " ":
        return "%20"
    
    arr = list(s) # O(n) space
    for i in range(len(arr)): # O(n) time
        # print(char)
        if arr[i] == " ":
            arr[i] = "%20"

    return "".join(arr) #O(n) time

# apprach 2 - O(n) and O(n)
# def urlify(s):
#     # base cases
#     if not s:
#         return s
#     if s == " ":
#         return "%20"
#     return s.replace(" ", "%20") # returns the copy of the string

print(urlify("John Smith Kaka"))
