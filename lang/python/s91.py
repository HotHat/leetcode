from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        ln = len(s)
        dp = [0] * (2 if ln < 2 else ln)

        for i in range(0, ln):
            if i == 0:
                if s[i] == '0':
                    return 0
                dp[i] = 1

            elif i == 1:
                if s[i] == '0':
                    if '2' < s[i - 1] <= '9':
                        return 0
                    else:
                        dp[i] = dp[i-1]
                else:
                    if '2' < s[i - 1] <= '9' or (s[i - 1] == '2' and '6' < s[i] <= '9'):
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-1] + 1
            else:
                if s[i] == '0':
                    if s[i - 1] == '0':
                        return 0
                    else:
                        if '2' < s[i-1] <= '9':
                            return 0
                        dp[i] = dp[i - 2]
                else:
                    if s[i - 1] == '0':
                        dp[i] = dp[i - 1]
                    else:
                        if '2' < s[i-1] <= '9' or (s[i-1] == '2' and '6' < s[i] <= '9'):
                            dp[i] = dp[i - 1]
                        else:
                            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[ln - 1]

