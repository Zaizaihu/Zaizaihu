# -*- coding:utf-8 -*-
'''
传入一个数组与一个整数，要求返回数组中两数之等于整数的下标
enumerate：用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
'''

def STF(nums, target):
    dct = {}
    for i, n in enumerate(nums):
        cp = target - n
        if cp in dct:
            return [dct[cp], i]
        else:
            dct[n] = i


a={4,5,6,7,8,9,10}
print(STF(a,13))