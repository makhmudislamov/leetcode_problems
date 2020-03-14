"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


def groupAnagrams(strs: [str]):

    groups = {}

    anagram = [0] * 26
    for word in strs:
        for char in word:
            # create anagram array
            index = ord(char) - 97
            anagram[index] += 1
        
        key_ana = "".join([str(char) for char in anagram])
        # print(key_ana)
        if key_ana in groups:
            groups[key_ana].append(word)
        else:
            groups[key_ana] = [word]
        anagram = [0] * 26
        
    return list(groups.values())

    
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
