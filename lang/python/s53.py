from typing import List


class Solution:
    """
    给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    子数组 是数组中的一个连续部分。
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = {}
        ln = len(nums)
        mx = 0

        for i in range(ln):
            if i == 0:
                dp[i] = nums[i]
                mx = dp[i]
            else:
                dp[i] = max(nums[i], dp[i - 1]+nums[i])
                mx = max(mx, dp[i])

        return mx


