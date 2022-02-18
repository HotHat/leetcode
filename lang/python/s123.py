from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = [0] * len(prices)
        sell1 = [0] * len(prices)
        buy2 = [0] * len(prices)
        sell2 = [0] * len(prices)
        buy1[0] = buy2[0] = -prices[0]
        sell1[0] = sell2[0] = 0

        for i in range(1, len(prices)):
            buy1[i] = max(buy1[i - 1], -prices[i])
            sell1[i] = max(sell1[i - 1], buy1[i - 1] + prices[i])
            buy2[i] = max(buy2[i - 1], sell1[i] - prices[i])
            sell2[i] = max(sell2[i - 1], buy2[i] + prices[i])

        i = len(prices) - 1
        return max([buy1[i], sell1[i], buy2[i], sell2[i]])


    def helper(self, s, e, prices):
        if s == e:
            return 0
        if e - s == 1:
            return max(prices[e] - prices[s], 0)

        mx = 0
        for i in range(s, e):
            # if s == 3 and i == 5 and e ==
            lf = self.helper(s, i, prices)
            rg = self.helper(i+1, e, prices)
            tl = prices[e] - prices[s]
            mx = max([
                      # 一次
                      tl,
                      # 左边次
                      lf,
                      # 右边两次
                      rg,
                      # 左右各一次
                      (prices[i] - prices[s]) + (prices[e] - prices[i+1]),
                      # 0次
                      0, mx])

            print(f"l: {s}, {i} ==> {lf}; r: {i+1}, {e} ==> {rg}  | max: {mx}")

        return mx
