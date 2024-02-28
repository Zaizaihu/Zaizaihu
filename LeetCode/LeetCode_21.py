# -*- coding:utf-8 -*-
'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
'''
class Solution:

    def merge_sort(self,a,b):
        if len(a) == 0 and len(b) == 0:
            return print("请输入内容")
        list = a + b
        list.sort()
        print(list)

    def merge_sorted(self,a,b):
        if len(a) == 0 and len(b) == 0:
            return print("请输入内容")
        list = a + b
        result = sorted(list)
        print(result)
    #
    #   链表！ 找机会想人请教
    # def merge(self,list1,list2):
    #     while list1 and list2:
    #         if list1.val() <= list2.val:
    #             p.next = list1
    #             list1 = list1.next
    #         else:
    #             p.next = list2
    #             list2 = list2.next
    #         p = p.next


l1 = [1,2,3]
l2 = [4,5,6]
Solution().merge(l1,l2)