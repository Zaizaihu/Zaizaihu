# -*- coding:utf-8 -*-
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
class Solution():
    def step(self,nuber:int):
        result = 0
        for i in range(2,nuber):
            result += i

        return result

print(Solution().step(7))