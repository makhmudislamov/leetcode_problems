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
# whats is the min and max reqs of bigO?
# do we have equal lenghts of lists - equal amount of teachers to students

def assign(s, t):
    res = {} # key is student and value is teacher

    sorted_students = sorted(s)
    sorted_teachers = sorted(t)

    print(sorted_students)
    print(sorted_teachers)

    
    

    # return res


s = [1, 5, 8, 14, 56, 12, 0, 98, 3]
t = [1, 2, 5, 7, 14, 56, 87]
print(assign(s, t))