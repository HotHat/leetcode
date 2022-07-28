import unittest
from helper import parse_binary_tree, print_tree, \
    parse_pre_order_tree, inorder_traver_recursive, in_order_iterate, \
    pre_order_recursive, pre_order_iterate, post_order_recursive, post_order_iterate, morris_in_order


class TestHelper(unittest.TestCase):
    def test_parse(self):
        t = parse_binary_tree('(3 (1) (5 (4 ) (6)))')
        print(t)
        print_tree(t)
        # import math
        # print(-math.inf)
        # print(math.inf)

    def test_parse2(self):
        root = parse_pre_order_tree([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])
        inorder_traver_recursive(root)

    def test_parse3(self):
        root = parse_binary_tree('(6 (5 (3 () (4))) (10 (7) (15)))')
        # print_tree(s)
        in_order_iterate(root)

    def test_parse3_1(self):
        root = parse_binary_tree('(1 (2 (4 () (6 (7) (8)))) (3 () (5)))')
        # print_tree(root)
        morris_in_order(root)

    def test_parse4(self):
        root = parse_binary_tree('(1 (2 (4 () (6 (7) (8)))) (3 () (5)))')
        # print_tree(s)
        pre_order_recursive(root)

    def test_parse4_1(self):
        root = parse_binary_tree('(1 (2 (4 () (6 (7) (8)))) (3 () (5)))')
        pre_order_iterate(root)
        print()
        in_order_iterate(root)

    def test_parse5(self):
        root = parse_binary_tree('(1 (2 (4 () (6 (7) (8)))) (3 () (5)))')
        # print_tree(s)
        post_order_recursive(root)

    def test_parse5_1(self):
        root = parse_binary_tree('(1 (2 (4 () (6 (7) (8)))) (3 () (5)))')
        # print_tree(s)
        post_order_iterate(root)
