import unittest

import lang.python.s1
import lang.python.s8
import lang.python.s22
import lang.python.s45
import lang.python.s53
import lang.python.s70
import lang.python.s91
import lang.python.s96
import lang.python.s104
import lang.python.s119
import lang.python.s121
import lang.python.s122
import lang.python.s123
from lang.python.helper import TestCase as Tc, TreeNode, parse_binary_tree, print_tree, parse_pre_order_tree


class TestSolution(unittest.TestCase):
    def test_s1(self):
        cases = [
            Tc(([2, 7, 11, 15], 9), [0, 1]),
            Tc(([3, 2, 4], 6), [1, 2]),
            Tc(([3, 3], 6), [0, 1]),
            Tc(([-3, 3], 0), [0, 1]),
        ]
        s = lang.python.s1.Solution()
        for case in cases:
            self.assertEqual(s.twoSum(case.input[0], case.input[1]), case.target)

    def test_s1_2(self):
        cases = [
            # Tc(([2, 7, 11, 15], 9), [0, 1]),
            # Tc(([3, 2, 4], 6), [1, 2]),
            Tc(([3, 2, 3], 6), [0, 2]),
            # Tc(([-3, 3], 0), [0, 1]),
        ]
        s = lang.python.s1.Solution()
        for case in cases:
            self.assertEqual(s.twoSum2(case.input[0], case.input[1]), case.target)

    def test_s8(self):
        cases = [
            # Tc("", 0),
            Tc("-0012a42", -12),
            Tc("-+12", 0),
            Tc("00000-42a1234", 0),
            Tc("21474836460", 2147483647),
            Tc("+-12", 0),
            Tc("+1", 1),
            Tc("+0", 0),
            Tc("-0", 0),
            Tc("-+-0", 0),
            Tc("123", 123),
            Tc(" 0123", 123),
            Tc("-123", -123),
            Tc("   -123", -123),
            Tc("a", 0),
            Tc("123a", 123),
            Tc("2147483647", 2147483647),
            Tc("2147483648", 2147483647),
            Tc("21474836490", 2147483647),
            Tc("-2147483647", -2147483647),
            Tc("-2147483648", -2147483648),
            Tc("-2147483649", -2147483648),
            Tc("-21474836490", -2147483648),

        ]
        s = lang.python.s8.Solution()
        for case in cases:
            self.assertEqual(case.target, s.myAtoi(case.input))

    def test_s22(self):
        cases = [
            Tc(1, ["()"]),
            Tc(2, ["(())", "()()"]),
            Tc(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
            Tc(4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())",
                   "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]),
            Tc(5, ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))",
                   "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()",
                   "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()",
                   "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()",
                   "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()",
                   "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"]),

            # 1 => 1
            # 2 => 2
            # 3 => 5
            # 4 => 14
        ]
        s = lang.python.s22.Solution()
        for case in cases:
            self.assertEqual(case.target, s.generateParenthesis(case.input))

    def test_s45(self):
        cases = [
            Tc([2, 3, 1, 1, 4], 2),
            Tc([2, 3, 0, 1, 4], 2),
            Tc([2, 1], 1),
            Tc([2, 3, 1], 1),
            Tc([1, 1, 1, 1], 3),
            Tc([1, 2, 1, 1, 1], 3),
            Tc([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 2),
            Tc([5, 3, 4, 4, 1, 0, 2, 0, 3, 1, 0, 0], 4),
            #  [0, 1, 1, 1, 1, 1
            #  [0, 1, 1, 1, 1, 1, 2, 2
            #  [0, 1, 1, 1, 1, 1, 2, 2, 3
            #  [0, 1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4]
        ]
        s = lang.python.s45.Solution()
        for case in cases:
            self.assertEqual(case.target, s.jump(case.input))

    def test_s53(self):
        cases = [
            Tc([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            Tc([1], 1),
            Tc([-1], -1),
            Tc([5, 4, -1, 7, 8], 23),
        ]
        s = lang.python.s53.Solution()
        for case in cases:
            self.assertEqual(case.target, s.maxSubArray(case.input))

    def test_s70(self):
        cases = [
            Tc(2, 2),
            Tc(3, 3),
        ]
        s = lang.python.s70.Solution()
        for case in cases:
            self.assertEqual(case.target, s.climbStairs(case.input))

    def test_s91(self):
        cases = [
            Tc("1", 1),
            Tc("12", 2),
            Tc("226", 3),
            Tc("0", 0),
            Tc("06", 0),
            Tc("301", 0),
            Tc("27", 1),
            Tc("11106", 2),
            Tc("11601010101", 0),
        ]
        s = lang.python.s91.Solution()
        for case in cases:
            self.assertEqual(case.target, s.numDecodings(case.input))

    def test_s96(self):
        cases = [
            Tc(10, 16796),
            Tc(5, 42),
            Tc(3, 5),
            Tc(2, 2),
            Tc(1, 1),
        ]
        s = lang.python.s96.Solution()
        for case in cases:
            self.assertEqual(case.target, s.numTrees(case.input))

    def test_s98(self):
        cases = [
            Tc(parse_binary_tree('(2 (1) (3)'), True),
            Tc(parse_binary_tree('(5 (1) (4 (3) (6)))'), False),
            Tc(parse_binary_tree('(5 (4) (6 (3) (7)))'), False),
            Tc(parse_binary_tree('(3 (1 (0) (2)) (5 (4) (6)))'), True),
            Tc(parse_binary_tree('(3 (1 (0) (2 () (3) )) (5 (4) (6)))'), False),
        ]
        import lang.python.s98
        s = lang.python.s98.Solution()
        for case in cases:
            # print_tree(case.input)
            self.assertEqual(case.target, s.isValidBST(case.input))

    def test_s99(self):
        cases = [
            # Tc(parse_pre_order_tree([1, 3, None, None, 2]), None),
            Tc(parse_pre_order_tree([3, 1, 4, None, None, 2]), None),
        ]
        import lang.python.s99
        s = lang.python.s99.Solution()
        for case in cases:
            print_tree(case.input)
            s.recoverTree(case.input)
            print_tree(case.input)
            # self.assertEqual(case.target, s.recoverTree(case.input))

    def test_s101(self):
        cases = [
            Tc(parse_pre_order_tree([1, 2, 2, 3, 4, 4, 3]), True),
            Tc(parse_pre_order_tree([1, 2, 2, None, 3, None, 3]), False),
            Tc(parse_pre_order_tree([1, 2, 3]), False),
            Tc(parse_pre_order_tree([1, 2, 2, 3, 4, 4, 3]), True),
        ]
        import lang.python.s101
        s = lang.python.s101.Solution()
        for case in cases:
            self.assertEqual(case.target, s.isSymmetric(case.input))

    def test_s104(self):
        cases = [
            Tc(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))), 3)
        ]
        s = lang.python.s104.Solution()
        for case in cases:
            self.assertEqual(s.maxDepth(case.input), case.target)

    def test_s119(self):
        cases = [
            Tc(3, [1, 3, 3, 1]),
            Tc(0, [1])
        ]
        s = lang.python.s119.Solution()
        for case in cases:
            self.assertEqual(case.target, s.getRow(case.input))

    def test_s121(self):
        cases = [
            Tc([7, 1, 5, 3, 6, 4], 5),
            # Tc([7, 6, 5, 3, 1, 1], 0),
        ]
        s = lang.python.s121.Solution()
        for case in cases:
            self.assertEqual(case.target, s.maxProfit(case.input))

    def test_s122(self):
        cases = [
            Tc([7, 1, 5, 3, 6, 4], 7),
            # Tc([7, 6, 5, 3, 1, 1], 0),
        ]
        s = lang.python.s122.Solution()
        for case in cases:
            self.assertEqual(case.target, s.maxProfit(case.input))

    def test_s123(self):
        cases = [
            Tc([3, 3, 5, 0, 0, 3, 1, 4], 6),
            Tc([0, 3, 1, 4], 6),
            Tc([1, 2, 3, 4, 5], 4),
            Tc([7, 6, 4, 3, 1], 0),
            Tc([3, 2, 6, 5, 0, 3], 7),
            Tc([1, 0, 3], 3),
            Tc([1, 3], 2),
            Tc([1], 0)
        ]
        s = lang.python.s123.Solution()
        for case in cases:
            self.assertEqual(case.target, s.maxProfit(case.input))
