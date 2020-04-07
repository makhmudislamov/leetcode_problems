"""
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

For example:

  my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
"""
import unittest


def merge_lists(my_list, alices_list):

    if not my_list and not alices_list:
        return []
    elif not my_list:
        return alices_list
    elif not alices_list:
        return my_list
    
    mine = len(my_list) - 1
    # Combine the sorted lists into one large sorted list
    my_list.extend([None]*len(alices_list)) # created extra space

    # setting pointers
    pointer = len(my_list) - 1
    al_pointer = len(alices_list) - 1


    # TIME AND SPACE - O(n+m) and O(1)?
    while mine >= 0 and al_pointer >= 0:
        if my_list[mine] < alices_list[al_pointer]:
            my_list[pointer] = alices_list[al_pointer]
            al_pointer -= 1
        elif my_list[mine] > alices_list[al_pointer]:
            my_list[pointer] = my_list[mine]
            mine -= 1
        else:
            my_list[pointer] = alices_list[al_pointer]
            mine -= 1
        pointer -= 1
    
    my_list[:al_pointer + 1] = alices_list[:al_pointer + 1]
    return my_list

    # HAS BUG
    # res = []
    # i = j = 0
    # while i <= len(my_list) - 1 and j <= len(alices_list) - 1:
    #     if my_list[i] < alices_list[j]:
    #         res.append(my_list[i])
    #     else:
    #         res.append(alices_list[j])

    #     i += 1
    #     j += 1
    # if j == len(alices_list):
    #     res.extend(my_list[i:])
    # elif i == len(my_list):
    #     res.extend(alices_list[j:])
    # return res




# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
