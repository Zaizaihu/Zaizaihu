# -*- coding:utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return print(False)
                stack.pop()
            else:
                stack.append(ch)

        return print("True")

Solution().isValid("{[]{}}")