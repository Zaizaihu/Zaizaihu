# -*- coding:utf-8 -*-
'''
传入一个数组与一个整数，要求返回数组中两数之等于整数的下标
enumerate：用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
'''



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dct = dict()
        for i ,num in enumerate(nums):
            ans = target - num
            if ans in dct:
                return print(dct[target - num],i)
            dct[nums[i]] = i

    def STF(self,nums, target):
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i

a=[4,5,6,7,8,9,10]
print(Solution().twoSum(a,18))