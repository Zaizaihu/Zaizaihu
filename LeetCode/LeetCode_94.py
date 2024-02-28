# -*- coding:utf-8 -*-
'''
给定一个二叉树的根节点 root ，返回 它的 中序 遍历
'''

class Solution:
    def inorderTraversal(self, root:list,res = []):
        # print(root)
        if len(root) > 1:
            root.pop()
            self.inorderTraversal(root)
        res.append(root)
        return res


nums = [1,3,5,2,7]
print(Solution().inorderTraversal(nums))