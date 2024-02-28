# -*- coding:utf-8 -*-
'''
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
'''

class Solution():
    def Delrepeti(self,numers:list):
        return set(numers)

    def forrepeti(self,numers:list):
        index = []
        for i in range(len(numers)):
            if numers[i] in index:
                continue
            else:
                index.append(numers[i])
        return index


numers = [1,2,3,4,5,5,6]
print(Solution().Delrepeti(numers))
print(Solution().forrepeti(numers))