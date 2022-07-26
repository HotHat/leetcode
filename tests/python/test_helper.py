import unittest
from helper import parse_binary_tree, print_tree, parse_pre_order_tree


class TestHelper(unittest.TestCase):
    def test_parse(self):
        t = parse_binary_tree('(3 (1 (0) (2 () (3))) (5 (4 ) (6)))')
        print(t)
        print_tree(t)
        # import math
        # print(-math.inf)
        # print(math.inf)

    def test_parse2(self):
        root = parse_pre_order_tree([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])
        print_tree(root)
