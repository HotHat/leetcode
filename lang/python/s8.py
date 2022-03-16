from typing import List


class Solution:
    """
   请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/string-to-integer-atoi
    """
    MAX_INT = 2 ** 31
    def myAtoi(self, s: str) -> int:
        cnt = 0
        state = 1
        is_positive = True
        for c in s:
            if state == 1:
                if c == ' ':
                    continue

                else:
                    if c == '-':
                        is_positive = False
                        state = 2
                        continue

                    if c == '+':
                        state = 2
                        continue

            if not self.is_num(c):
                return cnt if is_positive else -cnt
            else:
                state = 2

            cur = ord(c) - ord('0')
            # max = 100
            # cnt = 12
            # cur = 3
            if self.is_overflow(cnt, cur, is_positive):
                return self.MAX_INT - 1 if is_positive else -self.MAX_INT
            else:
                cnt = cnt * 10 + cur

        return cnt if is_positive else -cnt

    def is_overflow(self, cnt, cur, is_positive):
        tmp = self.MAX_INT - (1 if is_positive else 0)
        for i in range(10):
            tmp -= cnt
            if tmp < 0:
                return True
        return True if tmp - cur < 0 else False

    @staticmethod
    def is_num(c):
        if '0' <= c <= '9':
            return True
        return False



