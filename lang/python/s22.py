from typing import List


class Solution:
    """
    给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
    在「杨辉三角」中，每个数是它左上方和右上方的数的和。
    """
    def generateParenthesis(self, n: int) -> List[str]:
        ln = n * 2
        rs = []
        for i in range(ln):
            if len(rs) == 0:
                rs.append('(')
            else:
                tmp = []
                for r in rs:
                    # add (
                    l = r + '('
                    if self.is_valid(l, n):
                        tmp.append(l)

                    # add )
                    r = r + ')'
                    if self.is_valid(r, n):
                        tmp.append(r)

                    rs = tmp
        rs = list(filter(lambda x: self.is_complete(x), rs))
        return rs

    def is_complete(self, st):
        r = 0
        for i in st:
            if i == '(':
                r += 1
            elif i == ')':
                r -= 1

            if r < 0:
                return False
        return True if r == 0 else False

    def is_valid(self, st, lv):
        r = 0
        for i in st:
            if i == '(':
                r += 1
            elif i == ')':
                r -= 1

            if r < 0:
                return False
            if r > lv:
                return False
        return True



