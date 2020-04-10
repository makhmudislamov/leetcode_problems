"""
Chapter1, page 90
replace all spaces in string with %20
example
input: "John Smith"
output: "John%20Smith"
"""

# questions to ask:
# acceptable and optimal time and space
# modifying the input? ASCII?

# approach 1 - time and space >> O(n) and O(1)
# iterate over the string if the char is " " replace it with %20

# def urlify(s):
#     # base cases
#     if not s:
#         return s
#     if s == " ":
#         return "%20"

#     # for i in range(len(s)):
#     #     # print(char)
    #     if s[i] == " ":
    #         s[i] = "%20"

    # return s

# apprach 2 - O(n) and O(n)


def urlify(s):
    # base cases
    if not s:
        return s
    if s == " ":
        return "%20"
    return s.replace(" ", "%20") # returns the copy of the string

print(urlify("John Smith Kaka"))
