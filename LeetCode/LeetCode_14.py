# -*- coding:utf-8 -*-
'''
leetcode ：14
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
'''


class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""
        ans, count = strs[0], len(strs)
        for i in range(1, count):
            ans = self.lcp(ans, strs[i])
            if not ans:
                ans = "None"
                break

        return ans

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
a = ['hjwje','hjΩsuhebf','hwowr']
print(Solution().longestCommonPrefix(a))