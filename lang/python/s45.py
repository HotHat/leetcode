from typing import List


class Solution:
    """
    给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
    数组中的每个元素代表你在该位置可以跳跃的最大长度。
    你的目标是使用最少的跳跃次数到达数组的最后一个位置。
    假设你总是可以到达数组的最后一个位置。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/jump-game-ii
            Tc([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3),
    """

    def jump(self, nums: List[int]) -> int:
        # count = 0
        length = len(nums)
        cp = [0] * length

        if length == 1:
            return 0

        mx = nums[0]
        level = 1
        pos = 0
        while pos < length - 1:
            for i in range(pos+1, pos+mx):
                if cp[i] == 0:
                    cp[i] = level

            idx = pos+1
            # mx = nums
            for i in range(pos+mx, pos, -1):
                if nums[i] + (i - pos) > mx:
                    mx = nums[i]
                    idx = i
                self.add_level(i, i+nums[i], cp, level+1)

            pos = idx
            level += 1

        return level


        # while pos < length - 1:
        #     if pos + nums[pos] >= length:
        #         return count + 1
        #     idx = self.get_max_index(pos, pos + nums[pos], nums)
        #
        #     while nums[idx] == 0:
        #         idx = self.get_max_index(pos+1, idx-1, nums)
        #
        #     pos = idx
        #     count += 1
        #
        # return count

    def add_level(self, lf, rg, cp, level):
        for i in range(lf, rg):
            if cp[i] == 0:
                cp[i] = level

    def get_max_index(self, lf, rg, lst):
        mx = rg - lf + lst[rg]
        idx = rg
        for i in range(rg, lf, -1):
            if lst[i] + (i - lf) > mx:
                mx = lst[i]
                idx = i
        return idx



