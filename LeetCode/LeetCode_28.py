# -*- coding:utf-8 -*-
'''
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
'''
class Solutino:
    def return_str(self,haystack,needle):
        if needle not in haystack:
            return -1
        else:
            return haystack.find(needle)

haystack = "buhjifslaliulu"
needle = "liu"
print(Solutino().return_str(haystack,needle))