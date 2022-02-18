from typing import List


class Solution:
    """
    121. 买卖股票的最佳时机
    给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
    你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
    返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
    """

    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        sell[0] = 0

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], -prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return max(sell[len(prices) - 1], 0)
