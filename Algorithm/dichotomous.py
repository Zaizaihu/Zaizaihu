# -*- coding:utf-8 -*-
'''
leetcode:1552           二分算法
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有n个空的篮子，
第i个篮子的位置在position[i]，Morty想把m个球放到这些篮子里，使得任意两球间最小磁力最大。
已知两个球如果分别位于x和y，那么它们之间的磁力为|x - y|.
给你一个整数数组position和一个整数m，请你返回最大化的最小磁力。
'''
n = [1, 4, 2, 6, 8, 3, 42, 646, 94]
m = 3


class Solution:
    def maxDistance(self, position: [int], m: int) -> int:
        def check(x: int) -> bool:
            pre = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if position[i] - pre >= x:
                    pre = position[i]
                    cnt += 1
            return cnt >= m

        position.sort()
        left, right, ans = 1, position[-1] - position[0], -1
        while left <= right:
            mid = (left + right) // 2;
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

print(Solution().maxDistance(n, m))