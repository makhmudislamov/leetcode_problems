"""
I'm making a search engine called MillionGazillion™.

I wrote a crawler that visits web pages, stores a few keywords in a database, 
and follows links to other web pages. I noticed that my crawler was wasting a lot 
of time visiting the same pages over and over, so I made a set, visited, 
where I'm storing URLs I've already visited. Now the crawler only visits a URL if it hasn't already been visited.

Thing is, the crawler is running on my old desktop computer in my parents' 
basement (where I totally don't live anymore), and it keeps running out of memory because visited is getting so huge.

How can I trim down the amount of space taken up by visited?
"""

import unittest

class Node(object):
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.terminal = False

class Trie(object):
    def __init__(self):
        self.root = Node("")

    # Implement a trie and use it to efficiently store strings

    def contains(self, word):
        current = self.root

        for i, c in enumerate(word):
            if current.children.get(c) != None:
                current = current.children.get(c)

            if i == len(word) - 1 and current.terminal is True:
                return True
        return False

    def add_word(self, word):
        
        current_node = self.root
        if not self.contains(word):
            for i, c in enumerate(word):
                if current_node.children.get(c) == None:
                    current_node.children[c] = Node(c)
                current_node = current_node.children.get(c)
            
                if i == len(word) - 1 :
                    current_node.terminal = True
        return current_node.terminal



# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)
