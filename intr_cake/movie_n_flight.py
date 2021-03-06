"""
Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""

import unittest


def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    # questions to ask:
    # 1 - movies sorted?
    # 2 first combo?
    # 3 - exact sum?

    # target - flight lenght
    # find sum - in movies - exact?
    # PSEUDOCODE
    # if not sorted, sorted movies arr >> add it to set

    # set two pointers from the end and start of the set
    # based on when which pointer moves and sum gets closer to sum, move the pointers
    # return True/False
    if len(movie_lengths) == 0 or len(movie_lengths) == 1:
        return False

    # start = 0
    # end = len(movie_lengths) - 1
    # sorted_arr = sorted(movie_lengths) # O(nLogn)
    # while start < end: # O(n)
    #     two_movies_len = sorted_arr[start] + sorted_arr[end]

    #     if two_movies_len == flight_length:
    #         return True
    #     elif two_movies_len > flight_length:
    #         end -= 1
    #     else:
    #         start += 1

    # return False
    # Total time complexity >> n  + n Logn = nLogn

    # OPTIMIZATION

    seen_movies = set() # SPACE - O(n)

    for first_movie in movie_lengths: # TIME - O(n)
        second_movie = flight_length - first_movie

        if second_movie in seen_movies:
            return True
        seen_movies.add(first_movie)

    return False
    # TOTAL - SPACE and TIME - O(n)


# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
