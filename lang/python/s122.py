from typing import List


class Solution:
    """
    122. 买卖股票的最佳时机 II
    给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
    在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
    返回 你能获得的 最大 利润 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
    """

    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        sell[0] = 0

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], sell[i-1]-prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return max(sell[len(prices) - 1], 0)
