"""
Teachers and students are identified by an integer that represents their proficiency level.
Write a method to assign each student to the teacher of the closest level.
students
s = [ 1, 5, 8, 14, 56, 12, 0, 98, 3]
s = [0, 1, 3, 5, 8, 12, 14, 56, 98]
teachers
t = [1, 2, 5, 7, 87, 14, 56]
t = [1, 2, 5, 7, 14, 56, 87]
you can write to stdout for debugging purposes, e.g.

[(1, 1),(8, 7), (14, 14), (56, 56), (12, 14), (0,1), (98, 87), (3, 2)]
"""
# whats is the min and max reqs of bigO? - 
# do we have equal lenghts of lists - equal amount of teachers to students
# output: key, value >> teacher and student. 14: [12, 13]

def assign(s, t):
    # optimal: teacher = student
    # teacher = student +- 1

    # sort both arr
    # init dict
    # loop over both arr
    # if teacher == student >> add dict key value
    #  abs(teacher - student) = 1 >> add to dict
    # return dict

    #  nlogn
    t.sort()
    s.sort()
    
    res = {} 
    st_ind = 0
    t_ind = 0
    # n**2
    while st_ind < len(s):
        diff = float("inf") # setting global differnce between two scores
        while t_ind < len(t):
            current_diff = abs(t[t_ind] - s[st_ind]) # difference between two students
            # updating if current min is less then global min 
            if current_diff <= diff:
                diff = current_diff # 
            else: # we found the pair, if difference is greater than current diff
                break
            t_ind += 1 # moving to next teacher
    
        # adding to dict
        if t[t_ind-1] not in res:
            res[t[t_ind-1]] = [s[st_ind]]
        else:
            res[t[t_ind-1]].append(s[st_ind])
        st_ind += 1 # moving to next student
        t_ind = 0 # resetting teacher ind
    return res
``
# Time and Space >> O(n*m), O(n+m) - res

s = [1, 5, 8, 14, 56, 12, 0, 98, 3]
t = [1, 2, 5, 7, 14, 56, 87]
print(assign(s, t))
