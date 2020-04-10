"""
Chapter 1, page90

check if the string is a permutaiton of a pal
"""

# questions to ask:
#  acceptable and optimal time and space req
# case sensetivity, lower, uppercases - input can be upper case

# apprach 1 - O(n) space and time
# use set
# if char is in the set delete it
# if len of the set is less than or equal to 1 - permutation of a pal

def is_permi_pal(s):
    # base case
    if len(s) <= 1:
        return True
    s = s.lower()
    # "".join(s)
    print(s)
    check = set()

    for char in s:
        if char == " ":
            continue
        if char not in check:
            check.add(char)
        else:
            check.remove(char)

    return len(check) <= 1

print(is_permi_pal("Tact Coa"))
