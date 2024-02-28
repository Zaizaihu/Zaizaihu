# -*- coding:utf-8 -*-
''''"将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
0     6      12        18
1   5 7   11 13    17
2 4   8 10   14 16
3     9      15
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        f, i = 0, - 1
        res = ['' for _ in range(numRows)]
        for c in s:
            res[f] += c
            if f == 0 or f == numRows - 1:
                i = - i
            f += i
        return "".join(res)


str = "hujingwang"
nuber = 4
print(Solution().convert(str,nuber))