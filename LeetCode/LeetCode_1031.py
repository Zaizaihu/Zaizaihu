# -*- coding:utf-8 -*-
'''
leetcode：1031
给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。（这里需要澄清的是，长为 L 的子数组可以出现在长为 M 的子数组之前或之后。）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-of-two-non-overlapping-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def Sumoftwo(list:list):
    a = 0
    for i in range(len(list)-1):
        carry = list[i]+list[i+1]
        if carry > a:
            a = carry
    return a
a = [50,24,8,63,7]
print(Sumoftwo(a))