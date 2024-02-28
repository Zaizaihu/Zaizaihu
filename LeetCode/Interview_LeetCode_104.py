# -*- coding:utf-8 -*-
"面试题 0104"
'''
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
回文串不一定是字典当中的单词'''

text = "tactcoa"

List = {}
print(List)
for i in text:
    if i in List:
        List[i] += text.index
    else:
        List['%s'%(i)] = 1

