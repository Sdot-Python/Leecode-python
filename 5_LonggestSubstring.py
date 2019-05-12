# coding :utf-8
"""
未完待续1
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_dic = {}
        index_dic = {}
        flag  = ""
        for index,item in enumerate(s):
            if item not in index_dic:
                index_dic[item] = [index]
            else:
                index_dic[item].append(index)

        # [1,2,3]
        for item,indexs in index_dic.items():
            print(item,indexs)
            if len(indexs) == 1:
                continue
            if len(indexs) == 2:
                temp_str = s[indexs[0]:indexs[1]]
                if temp_str == temp_str[::-1]:
                    result_dic[len(temp_str)] = temp_str

            for index,item in enumerate(indexs):
                if index == len(indexs)-2:
                    break
                for item in indexs[index:]:
                    temp_str = s[item:indexs[index+1]]
                    if temp_str == temp_str[::-1]:
                        result_dic[len(temp_str)] = temp_str
        print(result_dic)
        print (sorted(result_dic.items(),key=lambda item:item[0]))

        # return result

if __name__ == '__main__':
    test = Solution()
    test.longestPalindrome("babad")