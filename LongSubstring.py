# -*- coding:utf-8 -*-
'''
leetcode：3
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
list.index(key)返回list中key的下标
'''
def lengthOfLongestSubstring(S:str):
    oct = []
    n = len(S)
    for i in range(n):
        if S[i] not in oct:
            oct.append(S[i])
        else:
            oct.append(S[i])
            rep = oct.index(S[i])
            for i in range(rep+1):
                oct.pop(0)
        print(oct)
    return oct

a = "sjfdinsrfgihs"
print(lengthOfLongestSubstring(a))