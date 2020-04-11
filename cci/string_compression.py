"""
Chapter1, page 90
implement basic string compression method using counts of repeated chars.
example
input: aabcccccaaa
output: a2bc5a3
if non compressable, return the input
input has only uppercase and lowercase letters (a-z)
"""

# questions to ask:
# acceptable and optimal time and space reqs


# base cases
#  if input is empty return empty string

# approach 1 - O(n) time and space
# init empty dict
# init empty string
# build dict with char and frequency
# loop over the dict
# add key,value as string to output

def compressor(s):
    if not s:
        return s
    if len(s) == 1:
        return s

    # frequency_map = {}
    # res = ""

    # for char in s:
    #     if char not in frequency_map:
    #         frequency_map[char] = 1
    #     else:
    #         frequency_map[char] += 1
            
    # print(frequency_map)
    # # for char, freq in frequency_map.items():
    # #     res += char
    # #     res += str(freq)

    # return res
    
    # plan b
    # init stack
    # init counter
    # increment counte


    stack = []
    res = ""
    for char in s:
        stack.append(char)
        
        if char != stack[0]:
            stack.pop()
  
            res += stack[0]
            res += str(len(stack))

            stack.clear()
            stack.append(char)
    
    res += stack[0]
    res += str(len(stack))
    
    return res


print(compressor("aabcccccaaa"))
