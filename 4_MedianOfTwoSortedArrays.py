# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 19:42
# @Author  : Sdot
# @Site    :
# @Software: PyCharm
"""
未完待续

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1 + nums2)
        half_length = length // 2
        temp_list = []
        flag1 = 0
        flag2 = 0
        if len(nums1) == 0:
            temp_list = nums2
        if len(nums2) == 0:
            temp_list = nums2

        if len(temp_list) == 0:
            for i in range(length * 2):
                if flag1 == len(nums1):
                    temp_list += nums2[flag2:]
                    break
                if flag2 == len(nums2):
                    temp_list += nums1[flag1:]
                    break
                if nums1[flag1] > nums2[flag2]:
                    temp_list.append(nums2[flag2])
                    flag2 += 1
                else:
                    temp_list.append(nums1[flag1])
                    flag1 += 1
        if len(temp_list) == 1:
            result = temp_list[0]
        elif length % 2 == 0:
            result = (temp_list[half_length] + temp_list[half_length-1])/2
        else:
            result = temp_list[half_length + 1]

        return result

if __name__ == '__main__':
    test = Solution()
    nums1 = []
    nums2 = [1]
    print(test.findMedianSortedArrays(nums1,nums2))