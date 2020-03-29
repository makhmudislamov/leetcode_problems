"""
Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 

Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
 

Note:

1 <= A.length <= 2000
0 <= A[i] <= 1000
"""


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        # build hashmap with occurances

        # iterate over the hashmap
        # insert all nums with one accurance to list
        # return max of that list

        if len(A) < 1 or not A:
            return -1
        count = {}

        for num in A:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        singles = []

        for num, _ in count.items():
            if count.get(num) == 1:
                singles.append(num)

        if len(singles) != 0:
            return max(singles)
        return -1
