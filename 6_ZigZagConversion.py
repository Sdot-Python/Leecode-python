#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:sdot
# datetime:2019/5/19 14:42
# software: PyCharm

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 1,n等于行数
        all_list = []

        # 有多少列
        if len(s) == 1 or numRows==1:
            return s
        all_s = (len(s) // (2 * numRows - 2) + 1) * (numRows - 1)
        index = 0  # 记录到哪一列了
        s_index = 0  # 记录到哪个元素了
        for i in range(1, all_s + 1):
            temp_str = ""
            # 如果是长的那一行
            if i == 1 or (i - 1) % (numRows - 1) == 0:
                prefix = index * (numRows + numRows - 2)
                temp_str = s[prefix:prefix + numRows]
                all_list.append(temp_str)
                print("i:{} len str:{}".format(i, temp_str))
                index += 1
                s_index += numRows
            else:

                # 开始计算结果
                if s_index >= len(s):
                    result = ""
                    for index in range(numRows):
                        for li in all_list:
                            try:
                                result += li[index]
                            except:
                                continue
                    return result.replace("*","")

                # 想办法算出一列中元素相对位置
                if s_index + 1 <= 2 * numRows - 2:
                    ss_index = numRows - (s_index + 1 - numRows)   # 总行数，减去元素相对于最低行的下标,得出列顺序下标
                else:
                    ss_index = numRows - ((s_index + 1) % (3 * numRows - 2))

                short_list = ""
                for i in range(numRows):
                    if i == ss_index-1:
                        short_list += s[s_index]
                    else:
                        short_list += "*"
                all_list.append(short_list)
                print("short index:{} str:{}".format(ss_index, temp_str))
                s_index += 1

        # 计算结果
        result = ""
        for index in range(numRows):
            for li in all_list:
                try:
                    result += li[index]
                except:
                    continue
        return result.replace("*","")

if __name__ == '__main__':
    test = Solution()
    print(test.convert("PAYPALISHIRING", 3))
