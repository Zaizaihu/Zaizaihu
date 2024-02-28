# -*- coding:utf-8 -*-
'''
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
'''
class Solution():
    def addsort(self,num,nuber,num_1,nuber_1):
        result = []
        for i in range(nuber):
            result.append(num[i])
        for j in range(nuber_1):
             result.append(num_1[j])
        result.sort()
        return result

    def cutmergesort(self,num,nuber,num_1,nuber_1):
        for i in range(nuber):
            if 0 in num:
                num.pop()
        for j in range(nuber_1):
            if 0 in num_1:
                num_1.pop()
        result = num + num_1
        result.sort()
        return result

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(Solution().addsort(nums1,m,nums2,n))
print(Solution().cutmergesort(nums1,m,nums2,n))