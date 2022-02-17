import unittest

import lang.python.s1
import lang.python.s104
import lang.python.s123
from lang.python.helper import TestCase as Tc, TreeNode


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

    def test_s104(self):
        cases = [
            Tc(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))), 3)
        ]
        s = lang.python.s104.Solution()
        for case in cases:
            self.assertEqual(s.maxDepth(case.input), case.target)

    def test_s123(self):
        cases = [
            # Tc([3, 3, 5, 0, 0, 3, 1, 4], 6),
            # Tc([0, 3, 1, 4], 6),
            # Tc([1, 2, 3, 4, 5], 4),
            # Tc([7, 6, 4, 3, 1], 0),
            Tc([3, 2, 6, 5, 0, 3], 7),
            # Tc([1, 0, 3], 3),
            # Tc([1, 3], 2),
            # Tc([1], 0)
        ]
        s = lang.python.s123.Solution()
        for case in cases:
            self.assertEqual(case.target, s.maxProfit(case.input))
