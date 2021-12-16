# -*- coding:utf-8 -*-
'''
leetcode：26
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。'''
#注意题目 "有序"

a = [1,4,2,6,3,3,6,3,4,4]
class Solution:
    def removeDuplicates(self, nums: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                fast += 1
            else:
                nums.pop(fast)
                fast += 1
                n -= 1
        return len(nums)
print(Solution().removeDuplicates(a))