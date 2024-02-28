# -*- coding:utf-8 -*-
#冒泡排序
a=[8616,8704,8670,9234,8922,8711,8716,8649,8661,8650,8718,8684,8900,8723,8641,8632,8633,8740,8635,8637,8636]
# def bubble(n :list):
#     for i in range(len(n)):
#         for j in range(i):
#             if n[i] < n[j]:
#                 n[i], n[j] = n[j], n[i]
#     return n
# print(bubble(a))
# # 实现快排
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    left,right,mid = [],[],nums.pop()

    for i in nums:
        if i <= mid:
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [mid] + quicksort(right)

print(quicksort(a))




