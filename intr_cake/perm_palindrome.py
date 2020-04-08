"""
Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"But 'ivicc' isn't a palindrome!"

If you had this thought, read the question again carefully. We're asking if any permutation of the string is a palindrome.
 Spend some extra time ensuring you fully understand the question before starting. 
 Jumping in with a flawed understanding of the problem doesn't look good in an interview.
"""
import unittest


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    # Time and Space - O(n) dict, O(n) space
    # build a dict to store ocuurance of each letter in the word

    # loop over the word
    # if len of the word is even and occurance of each letter should be even always - True
    # if len of the word is odd and occurance of only one letter can be not even  - True
    if len(the_string) < 1:
        return True
    letters = {}
    # building dict
    for c in the_string:
        if c not in letters:
            letters[c] = 1
        else:
            letters[c] += 1
    print(letters)
    len_check = len(the_string) % 2
    counter = 0
    for c, o in letters.items():
        occ_check = o % 2
        if len_check == 0 and occ_check != 0:
            return False

        if len_check != 0:
            if occ_check != 0:
                counter += 1
        
    if len_check != 0 and counter != 1:
        return False
    


    return True



# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
