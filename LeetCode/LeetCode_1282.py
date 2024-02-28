# -*- coding:utf-8 -*-
'''看不懂题目要求

有 n 个人被分成数量未知的组。每个人都被标记为一个从 0 到 n - 1 的唯一ID。

给定一个整数数组 groupSizes ，其中 groupSizes[i] 是第 i 个人所在的组的大小。例如，如果 groupSizes[1] = 3 ，
则第 1 个人必须位于大小为 3 的组中。

返回一个组列表，使每个人 i 都在一个大小为groupSizes[i]的组中。

每个人应该恰好只出现在一个组中，并且每个人必须在一个组中。如果有多个答案，
返回其中任何一个。可以保证给定输入至少有一个 有效的解。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/group-the-people-given-the-group-size-they-belong-to
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution:
    def groupThePeople(self, groupSizes: [int]) :
        groups = [[],[]]
        for i, size in enumerate(groupSizes):
            print(i,groups,"这是gruops")
            groups[i].append(size)
        ans = []
        for size, people in groups.items():
            ans.extend(people[i: i + size] for i in range(0, len(people), size))
        return ans
        # return groups
List = [1,3,3,1,1,2]
print(Solution().groupThePeople(List))