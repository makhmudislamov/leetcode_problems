"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""



def reorderLogFiles( logs: [str]):
#   O(n) time and size solution (if output is not considered its O(1) size)
#   create output arr size of input
# have two pointers one from start and one from end
# iterate over the input
# when let is found start filling the output arr from the end
# and when dig is found fill the output arr from the arr
# increment/decrement two pointers
# return output arr

# corrections
# itertate twice first fill with letter logs then digit logs to keep dig log order
    # res = [0] * len(logs)
    # start, end = 0, len(res)-1
    # while start < end:
    #     print(res)
    #     for s in logs:  
    #         if not s.split()[len(s.split())-1].isdigit():
    #             res[start] = s
    #             start += 1
    #     for s in logs:
    #         if s.split()[len(s.split())-1].isdigit():
    #             res[start] = s
    #             start += 1
    # return res

    def f(log):
        id_, rest = log.split(" ", 1)
        print(rest[0])
        return (0, rest, id_) if rest[0].isalpha() else (1,)
    
    return sorted(logs, key = f)



logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

print(reorderLogFiles(logs))
