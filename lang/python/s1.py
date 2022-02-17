from typing import List


class Solution:
    """
    1. 两数之和
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

    你可以按任意顺序返回答案。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/two-sum
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        dup_map = {}
        for (idx, val) in enumerate(nums):
            index_map[val] = idx
            dup_map[val] = 1+dup_map[val] if val in dup_map else 1

        for (idx, i) in enumerate(nums):
            sub = target - i
            dup_map[i] -= 1
            if sub in index_map and dup_map[sub] > 0:
                return [idx, index_map[sub]]

        assert False

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for (idx, val) in enumerate(nums):
            if val in index_map:
                return [index_map[val], idx]
            sub = target - val
            index_map[sub] = idx

        assert False


