from typing import List


class Solution:
    """
    给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
    在「杨辉三角」中，每个数是它左上方和右上方的数的和。
    """
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        lf = ["("] * n
        rg = [")"] * n

        p = lf + rg
        rs = ["".join(p)]

        for i in range(n-1, 0, -1):
            for j in range(n, 2*n-1):
                p[i] = ')'
                p[j] = '('
                rs.append("".join(p))
                p[i] = '('
                p[j] = ')'

        print(rs)
        return rs



