import unittest

import lang.python.s1
from lang.python.helper import TestCase as Tc


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


