#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 19:56
# @Author  : Aries
# @Site    :
# @File    : single_linked_list.py
# @Software: PyCharm

# 复习Python数据结构构建链表代码


class SingleNode(object):
    def __init__(self, element):
        # 节点拥有两个值,元素值以及连接域
        self.element = element
        self.next = None


class SinglelinkList(object):
    """构建单链表"""

    def __init__(self):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        count = 0
        current = self.__head
        while current != None:
            count += 1
            current = current.next
        return count

    # 遍历整个节点
    def travel(self):
        current = self.__head
        while current != None:
            print (current.element)
            current = current.next

    # 像链表的头部添加元素
    def add(self,item):
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    # 像链表的尾部添加元素
    def append(self,item):
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node

        else:
            current = self.__head
            while current != None:
                current = current.next
            current.next = node