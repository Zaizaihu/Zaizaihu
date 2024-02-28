# -*- coding:utf-8 -*-
'''
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
'''

class Solution():
    def fc(self,nuber:int):
        for i in range(0,nuber):
            if nuber < i * i:
                return i-1

print(Solution().fc(8))