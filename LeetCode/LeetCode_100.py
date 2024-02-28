# -*- coding:utf-8 -*-
'''
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
'''
class Solution():
    def seemtree(self,nums:list,nums_1:list):
        if len(nums) != len(nums_1):
            return False
        for i in range(len((nums))):
            if nums[i] != nums_1[i]:
                return False
        return True

p = [1,3,4,5,5]
q = [1,3,5,5]
print(Solution().seemtree(q,p))