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
from lang.python.helper import TestCase as Tc, TreeNode, parse_binary_tree, print_tree, \
    parse_pre_order_tree, get_binary_level


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
            Tc([parse_pre_order_tree([1, 2, 3]), parse_pre_order_tree([1, 2, 3])], True),
            Tc([parse_pre_order_tree([1, 2]), parse_pre_order_tree([1, None, 2])], True),
            Tc([parse_pre_order_tree([1, 2, 1]), parse_pre_order_tree([1, 1, 2])], True),
        ]
        import lang.python.s100
        s = lang.python.s100.Solution()
        for case in cases:
            self.assertEqual(case.target, s.isSameTree(case.input[0], case.input[1]))

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

    def test_s103(self):
        cases = [
            Tc(parse_pre_order_tree([3, 9, 20, None, None, 15, 7]), [[3], [20, 9], [15, 7]]),
            Tc(parse_pre_order_tree([1]), [[1]]),
            Tc(parse_pre_order_tree([]), []),
        ]
        import lang.python.s103
        s = lang.python.s103.Solution()
        for case in cases:
            self.assertEqual(case.target, s.zigzagLevelOrder(case.input))

    def test_s104(self):
        cases = [
            Tc(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))), 3)
        ]
        s = lang.python.s104.Solution()
        for case in cases:
            self.assertEqual(s.maxDepth(case.input), case.target)

    def test_s105(self):
        cases = [
            Tc([[20, 15, 7], [15, 20, 7]], [20, 15, 7]),
            Tc([[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], [3, 9, 20, None, None, 15, 7]),
            Tc([[-1], [-1]], [-1]),
        ]
        import lang.python.s105
        s = lang.python.s105.Solution()
        for case in cases:
            r = get_binary_level(s.buildTree(case.input[0], case.input[1]))
            self.assertEqual(case.target, r)

    def test_s106(self):
        cases = [
            Tc([[9, 3, 15, 20, 7], [9, 15, 7, 20, 3]], [3, 9, 20, None, None, 15, 7]),
            Tc([[-1], [-1]], [-1]),
        ]
        import lang.python.s106
        s = lang.python.s106.Solution()
        for case in cases:
            r = get_binary_level(s.buildTree(case.input[0], case.input[1]))
            self.assertEqual(case.target, r)

    def test_s107(self):
        cases = [
            Tc(parse_pre_order_tree([3, 9, 20, None, None, 15, 7]), [[15, 7], [9, 20], [3]]),
            Tc(parse_pre_order_tree([1]), [[1]]),
            Tc(parse_pre_order_tree([]), []),
        ]
        import lang.python.s107
        s = lang.python.s107.Solution()
        for case in cases:
            self.assertEqual(case.target, s.levelOrderBottom(case.input))

    def test_s109(self):
        from helper import ListNode
        cases = [
            Tc(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9, None))))), [0, -3, 9, -10, None, 5]),
            Tc(None, []),
        ]
        import lang.python.s109
        s = lang.python.s109.Solution()
        for case in cases:
            r = get_binary_level(s.sortedListToBST(case.input))
            print(r)
            self.assertEqual(case.target, r)

    def test_s110(self):
        from helper import ListNode
        cases = [
            # Tc(parse_pre_order_tree([3, 9, 20, None, None, 15, 7]), True),
            # Tc(parse_pre_order_tree([1, 2, 2, 3, 3, None, None, 4, 4]), False),
            Tc(parse_pre_order_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4]), False),
            # Tc(None, True),
        ]
        import lang.python.s110
        s = lang.python.s110.Solution()
        for case in cases:
            self.assertEqual(case.target, s.isBalanced(case.input))

    def test_s111(self):
        from helper import ListNode
        cases = [
            # Tc(parse_pre_order_tree([3, 9, 20, None, None, 15, 7]), 2),
            Tc(parse_pre_order_tree([2, None, 3, None, 4, None, 5, None, 6]), 5),
        ]
        import lang.python.s111
        s = lang.python.s111.Solution()
        for case in cases:
            self.assertEqual(case.target, s.minDepth(case.input))

    def test_s112(self):
        from helper import ListNode
        cases = [
            Tc([parse_pre_order_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22], True),
            Tc([parse_pre_order_tree([1, 2, 3]), 5], False),
            Tc([parse_pre_order_tree([]), 0], False),
        ]
        import lang.python.s112
        s = lang.python.s112.Solution()
        for case in cases:
            self.assertEqual(case.target, s.hasPathSum(case.input[0], case.input[1]))

    def test_s113(self):
        cases = [
            Tc(parse_pre_order_tree([1, 2, 5, 3, 4, None, 6]), [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
            # Tc(parse_pre_order_tree([]), []),
            # Tc(parse_pre_order_tree([0]), [0]),
        ]
        import lang.python.s114
        s = lang.python.s114.Solution()
        for case in cases:
            # print_tree(case.input)
            s.flatten(case.input)
            print_tree(case.input)
            p = get_binary_level(case.input)
            self.assertEqual(case.target, p)

    def test_s116(self):
        cases = [
            Tc(parse_pre_order_tree([1, 2, 3, 4, 5, 6, 7]), [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']),
        ]
        import lang.python.s116
        s = lang.python.s116.Solution()
        for case in cases:
            # print_tree(case.input)
            p = s.connect(case.input)
            # s.connect(case.input)
            # p = get_binary_level(case.input)
            self.assertEqual(case.target, p)

    def test_s117(self):
        cases = [
            Tc(parse_pre_order_tree([1, 2, 3, 4, 5, None, 7]), [1, '#', 2, 3, '#', 4, 5, 6, 7, '#']),
        ]
        import lang.python.s117
        s = lang.python.s117.Solution()
        for case in cases:
            # print_tree(case.input)
            p = s.connect(case.input)
            # s.connect(case.input)
            # p = get_binary_level(case.input)
            self.assertEqual(case.target, p)

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

    def test_s124(self):
        cases = [
            Tc(parse_pre_order_tree([1, 2, 3]), 6),
            Tc(parse_pre_order_tree([-10, 9, 20, None, None, 15, 7]), 42),
            Tc(parse_pre_order_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 48),
        ]
        import lang.python.s124
        s = lang.python.s124.Solution()
        for case in cases:
            print_tree(case.input)
            self.assertEqual(case.target, s.maxPathSum(case.input))

    def test_s129(self):
        cases = [
            # Tc(parse_pre_order_tree([1, 2, 3]), 25),
            Tc(parse_pre_order_tree([4, 9, 0, 5, 1]), 1026),
        ]
        import lang.python.s129
        s = lang.python.s129.Solution()
        for case in cases:
            self.assertEqual(case.target, s.sumNumbers(case.input))

    def test_s173(self):
        cases = [
            Tc(parse_pre_order_tree([7, 3, 15, None, None, 9, 20]), [3, 7, True, 9, True, 15, True, 20, False]),
        ]
        from lang.python.s173 import BSTIterator
        for case in cases:
            r = []
            bSTIterator = BSTIterator(case.input)
            r.append(bSTIterator.next())
            r.append(bSTIterator.next())
            r.append(bSTIterator.hasNext())
            r.append(bSTIterator.next())
            r.append(bSTIterator.hasNext())
            r.append(bSTIterator.next())
            r.append(bSTIterator.hasNext())
            r.append(bSTIterator.next())
            r.append(bSTIterator.hasNext())
            self.assertEqual(case.target, r)
