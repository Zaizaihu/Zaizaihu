# -*- coding:utf-8 -*-
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
'''
class Solution:
    def found(self,nums,target):
        if target in nums:
            return nums.find(target)
        else:
            for i in range(len(nums)):
                if target <= nums[i]:
                    nums.insert(target,i)
                    return i

nums = [1,2,4,5,7,8]
target = 6
print(Solution().found(nums,target))