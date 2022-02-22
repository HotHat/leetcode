from typing import List


class Solution:
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    """
    def climbStairs(self, n: int) -> int:
        dp = {
            0: 1,
            1: 1,
            2: 2
        }
        if n < 3:
            return dp[n]

        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]





