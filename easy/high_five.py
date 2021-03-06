"""
Given a list of scores of different students, return the average score of 
each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  
The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
"""

def highFive(items):
    """
    :type items: List[List[int]]
    :rtype: List[List[int]]
    """
    items = sorted(items)
    average_5 = []
    output = []
    print(items)
    for _id, score in items:
        average_5.append(score)
        if len(average_5) == 5:
            output = [_id, sum(average_5) // 5]
    return output
        

# items = [[1, 91], [1, 92], [1, 60], [1, 65], [1, 87], [1, 100]]
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
    2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]

print(highFive(items))


