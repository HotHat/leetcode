from typing import List


class Solution:
    """
    给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
    在「杨辉三角」中，每个数是它左上方和右上方的数的和。
    """
    def getRow(self, rowIndex: int) -> List[int]:
        dp = {
            0: [1],
            1: [1, 1]
        }
        if rowIndex < 2:
            return dp[rowIndex]

        for i in range(2, rowIndex+1):
            row = [1]
            for j in range(len(dp[i - 1])-1):
                row.append(dp[i-1][j]+dp[i-1][j+1])

            row.append(1)

            dp[i] = row

        return dp[rowIndex]



