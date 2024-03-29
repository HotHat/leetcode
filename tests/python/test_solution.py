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

    def test_s199(self):
        cases = [
            # Tc(parse_pre_order_tree([1, 2, 3]), 25),
            # Tc(parse_pre_order_tree([1, 2, 3, None, 5, None, 4]), [1, 3, 4]),
            Tc(parse_pre_order_tree([1, 2, 3, None, 5, None, 4]), [1, 3, 4]),
            Tc(parse_pre_order_tree([1, None, 3]), [1, 3]),
            Tc(parse_pre_order_tree([]), []),
        ]
        import lang.python.s199
        s = lang.python.s199.Solution()
        for case in cases:
            # print_tree(case.input)
            self.assertEqual(case.target, s.rightSideView(case.input))

    def test_s222(self):
        cases = [
            Tc(parse_pre_order_tree([1, 2, 3, 4, 5, 6]), 6),
            Tc(parse_pre_order_tree([]), 0),
            Tc(parse_pre_order_tree([1]), 1),
            Tc(parse_pre_order_tree([1, 2, 3, 4, 5, 6, 7]), 7),
        ]
        import lang.python.s222
        s = lang.python.s222.Solution()
        for case in cases:
            self.assertEqual(case.target, s.countNodes(case.input))

    def test_s226(self):
        cases = [
            # Tc(parse_pre_order_tree([4, 2, 7, 1, 3, 6, 9]), []),
            Tc([parse_pre_order_tree([3, 1, 4, None, 2]), 1], 1),
            Tc([parse_pre_order_tree([5, 3, 6, 2, 4, None, None, 1]), 3], 3),
        ]
        import lang.python.s230
        s = lang.python.s230.Solution()
        for case in cases:
            # print_tree(case.input)
            r = s.kthSmallest(case.input[0], case.input[1])
            self.assertEqual(case.target, r)

    def test_s235(self):
        cases = [
            # Tc(parse_pre_order_tree([4, 2, 7, 1, 3, 6, 9]), []),
            Tc([parse_pre_order_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), 2, 5], 1),
            # Tc([parse_pre_order_tree([5, 3, 6, 2, 4, None, None, 1]), 3], 3),
        ]
        import lang.python.s235
        s = lang.python.s235.Solution()
        for case in cases:
            # print_tree(case.input)
            r = s.lowestCommonAncestor(case.input[0], case.input[1], case.input[2])

    def test_s257(self):
        cases = [
            Tc(parse_pre_order_tree([1, 2, 3, None, 5]), ["1->2->5", "1->3"]),
            Tc(parse_pre_order_tree([1]), ["1"]),
        ]
        import lang.python.s257
        s = lang.python.s257.Solution()
        for case in cases:
            # print_tree(case.input)
            r = s.binaryTreePaths(case.input)
            self.assertEqual(case.target, r)

    def test_s297(self):
        case = parse_pre_order_tree([1, 2, -13, None, None, 4, 5])
        import lang.python.s297
        s = lang.python.s297.Codec()
        r1 = s.serialize(case)
        print(r1)
        # print_tree(case)

        r = s.deserialize(r1)
        # print(r)
        # print(s.serialize(r))
        # print_tree(r)
        self.assertEqual(r1, s.serialize(r))

    def test_331(self):
        cases = [
            '9,3,4,#,#,1,#,#,2,#,6,#,#',
            '1,#',
            '9,#,#,1',
            '#',
            '1,#,#,#,#',
            "#,7,6,9,#,#,#",
            "9,3,4,#,#,1,#,#,#,2,#,6,#,#"
        ]
        import lang.python.s331
        s = lang.python.s331.Solution()
        for case in cases:
            r1 = s.isValidSerialization(case)
            print(r1)
        # print_tree(case)

    def test_337(self):
        cases = [
            # [3, 2, 3, None, 3, None, 1]
            [79, 99, 77, None, None, None, 69, None, 60, 53, None, 73, 11, None, None, None, 62, 27, 62, None, None, 50, 98, None, None, 90, 48, 82, None, None, None, 55, 64, None, None, 73, 56, 6, 47, None, 93, None, None, 75, 44, 30, 82, None, None, None, None, None, None, 57, 36, 89, 42, None, None, 76, 10, None, None, None, None, None, 32, 4, 18, None, None, 1, 7, None, None, 42, 64, None, None, 39, 76, None, None, 6, None, 66, 8, 96, 91, 38, 38, None, None, None, None, 74, 42, None, None, None, 10, 40, 5, None, None, None, None, 28, 8, 24, 47, None, None, None, 17, 36, 50, 19, 63, 33, 89, None, None, None, None, None, None, None, None, 94, 72, None, None, 79, 25, None, None, 51, None, 70, 84, 43, None, 64, 35, None, None, None, None, 40, 78, None, None, 35, 42, 98, 96, None, None, 82, 26, None, None, None, None, 48, 91, None, None, 35, 93, 86, 42, None, None, None, None, 0, 61, None, None, 67, None, 53, 48, None, None, 82, 30, None, 97, None, None, None, 1, None, None]
        ]
        import lang.python.s337
        s = lang.python.s337.Solution()
        for case in cases:
            root = parse_pre_order_tree(case)
            r1 = s.rob(root)
            print(r1)
        # print_tree(case)

    def test_404(self):
        cases = [
            # Tc(parse_pre_order_tree([3, 2, 3, None, 3, None, 1]), 7),
            Tc(parse_pre_order_tree([3, 9, 20, None, None, 15, 7]), 24),
            Tc(parse_pre_order_tree([1]), 0),
            Tc(parse_pre_order_tree([1, 2, 3, 4, 5]), 4),
        ]
        import lang.python.s404
        s = lang.python.s404.Solution()
        for case in cases:
            # print_tree(case.input)
            r = s.sumOfLeftLeaves(case.input)
            self.assertEqual(case.target, r)

    def test_437(self):
        cases = [
            # Tc(parse_pre_order_tree([3, 2, 3, None, 3, None, 1]), 7),
            # Tc((parse_pre_order_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8), 3),
            Tc((parse_pre_order_tree([1, -2, -3, 1, 3, -2, None, -1]), -1), 4),

        ]
        import lang.python.s437
        s = lang.python.s437.Solution()
        for case in cases:
            # print_tree(case.input)
            r = s.pathSum(case.input[0], case.input[1])
            self.assertEqual(case.target, r)

    def test_s449(self):
        case = parse_pre_order_tree(
            [41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, None, 43, 46, 49, 0, 2, 30, 36, None, None, None, None, None,
             None, 45, 47, None, None, None, None, None, 4, 29, 32, None, None, None, None, None, None, 3, 9, 26, None,
             31, 34, None, None, 7, 11, 25, 27, None, None, 33, None, 6, 8, 10, 16, None, None, None, 28, None, None, 5,
             None, None, None, None, None, 15, 19, None, None, None, None, 12, None, 18, 20, None, 13, 17, None, None,
             22, None, 14, None, None, 21, 23])
        import lang.python.s449
        s = lang.python.s449.Codec()
        r1 = s.serialize(case)
        # print(r1)
        # print_tree(case)

        r = s.deserialize(r1)
        # print(r)
        print(s.serialize(r))
        # print_tree(r)
        # self.assertEqual(r1, s.serialize(r))

    def test_s450(self):
        case = parse_pre_order_tree([3, 2, 4, 1])
        print_tree(case)
        import lang.python.s450
        s = lang.python.s450.Solution()
        r = s.deleteNode(case, 2)
        print_tree(r)
        import lang.python.s297
        s = lang.python.s297.Codec()
        r1 = s.serialize(r)
        print(r1)
