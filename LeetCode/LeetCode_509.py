# -*- coding:utf-8 -*-
'''
leetcode ：509
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
'''
def fbnq(n : int):
    if n < 1:
        return 0
    f1 = 0
    f2 = 1
    total = 0
    for i in range(n):
        total = f1 + f2
        f1 = f2
        f2 = total
    return total
print(fbnq(6))