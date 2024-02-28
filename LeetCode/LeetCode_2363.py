# -*- coding:utf-8 -*-
'''
给你两个二维整数数组items1 和items2，表示两个物品集合。每个数组items有以下特质：

items[i] = [valuei, weighti] 其中 valuei 表示第 i 件物品的 价值 ，weighti 表示第 i 件物品的 重量 。
items 中每件物品的价值都是 唯一的 。
请你返回一个二维数组 ret，其中 ret[i] = [valuei, weighti]， weighti 是所有价值为 valuei 物品的 重量之和 。
注意：ret 应该按价值 升序 排序后返回。

首先，Python里，list即列表，是一个容器，它可以用来装各种类型的数据。比如：listExample = [1, 'a', True]
# 然后随意添加元素
listExample.append(2)
listExample.append(False)
listExample.append('b')

但有时候，我们希望限定list里的元素，不能什么东西都随便往里塞，
所以用类型标注，来告诉编辑器list里元素的类型，比如，list里只能是int类型，那就标注list[int]：listOfInt: list[int] = []

Counter() 是 collections 库中的一个函数，
用来统计一个 python 列表、字符串、元组等可迭代对象中每个元素出现的次数，并返回一个字典。

items:函数以列表返回可遍历的(键, 值) 元组数组常与for循环搭配
'''
from collections import Counter
items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]

class Solution:
    def mergeSimilarItems(self, items1:list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        map = Counter()
        for a, b in items1:
            map[a] += b
        for a, b in items2:
            map[a] += b
        return sorted([a, b] for a, b in map.items())

print(Solution().mergeSimilarItems(items1,items2))