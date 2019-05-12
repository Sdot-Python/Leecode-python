# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 19:42
# @Author  : Sdot
# @Site    :
# @File    : 1,1_TwoSum.py
# @Software: PyCharm
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        [2,4,3]
        [5,6,4]
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        l3 = temp
        carry = 0
        while l1 or l2 or carry:
            # add 为对应位数上相加的和
            # carry 为对应位数的前一位加一
            add, carry = carry, 0
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            if add > 9:
                add -= 10
                carry = 1
            l3.next = ListNode(add)
            l3 = l3.next
        return temp.next