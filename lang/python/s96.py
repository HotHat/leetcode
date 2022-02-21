from typing import List


class Solution:
    dp = {}
    def numTrees(self, n: int) -> int:
        self.dp[0] = 1
        self.dp[1] = 1

        if n in self.dp:
            return self.dp[n]

        for i in range(1, n+1):
            if n not in self.dp:
                self.dp[n] = 0
            self.dp[n] += self.numTrees(i-1) * self.numTrees(n-i)

        return self.dp[n]

