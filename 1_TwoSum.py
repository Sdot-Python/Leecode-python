# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 19:42
# @Author  : Sdot
# @Site    :
# @File    : 1,1_TwoSum.py
# @Software: PyCharm

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
example:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 加上枚举,取出下标
        for index, num in enumerate(nums):
            for i in range(index, len(nums)):
                if i != index:
                    if num + nums[i] == target:
                        return [index, i]

    def run(self):
        result = self.twoSum([-1, -2, -3, -4, -5], -8)
        print(result)


if __name__ == '__main__':
    test = Solution()
    test.run()