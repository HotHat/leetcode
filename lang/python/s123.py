from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(0, len(prices) - 1, prices)

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
