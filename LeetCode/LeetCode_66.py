# -*- coding:utf-8 -*-
'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
'''

class Solution:
    def Add_1(self,nums:list):
        if not nums:
            return "请传入内容"
        nums[-1] = nums[-1] + 1
        return nums

nums = [0]
print(Solution().Add_1(nums))