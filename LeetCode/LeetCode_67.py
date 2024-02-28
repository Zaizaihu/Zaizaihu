# -*- coding:utf-8 -*-
'''
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
'''

class Solution:
    def addBinary(self, a, b):
        index = a + b
        rs = str(index)
        result = []
        for i in range(len(rs)):
            result += rs[i]
        for i in range(len(result)):
            if int(result[-i]) > 1:
                result[-i] = int(result[-i]) - 2
                result[-i-1] = int(result[-i-1]) + 1
        if result[0] == 2:
            result[0]= 10

        ans = ''
        for i in  range(len(result)):
            ans += str(result[i])
        return ans

number = 111111
number2 = 1110100
print(Solution().addBinary(number,number2))