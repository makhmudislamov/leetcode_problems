"""
I opened up a dictionary to a page in the middle and started 
flipping through, looking for words I didn't know. I put each word I didn't know at 
increasing indices in a huge list I created in memory. When I reached the end of the dictionary, 
I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, 
except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," 
which is where I started working from the beginning of the dictionary. 
This list is huge (there are lots of words I don't know) so we want to be efficient here.
"""
import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    # use binary search
    # declare target
    # until you find the target 
    # compare if the current postition is less or greater than the target
    # if current is less than target - ignore the rest
    # same if its greater  

    first_word = words[0]
    floor_ind = 0
    ceiling_ind = len(words) - 1

    while floor_ind < ceiling_ind:
        guess_ind = floor_ind + ((ceiling_ind - floor_ind) // 2)

        if words[guess_ind] >= first_word:
            floor_ind = guess_ind
        else:
            ceiling_ind = guess_ind

        if floor_ind + 1 == ceiling_ind:
            return ceiling_ind

    



# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
