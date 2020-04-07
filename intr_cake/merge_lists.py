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
    

    # Combine the sorted lists into one large sorted list
    output = []
    i = j = 0
    for i in range(len(my_list)-1):
        for j in range(len(alices_list)-1):
            if my_list[i] > alices_list[j]:
                output.append(alices_list[j])
            else:
                output.append(my_list[i])

    if j == len(alices_list)-1:
        for k in range(j, len(my_list)-1):
            output.append(my_list[k])
    
    if i == len(my_list)-1:
        for l in range(i, len(alices_list)-1):
            output.append(alices_list[l])

    return output



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
