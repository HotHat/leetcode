import unittest
from helper import parse_binary_tree, print_tree


class TestHelper(unittest.TestCase):
    def test_parse(self):
        t = parse_binary_tree('(5 (1) '
                              '   (4 (3) '
                              '      (6)))')
        print(t)
        print_tree(t)
