# # -*- coding:utf-8 -*-
'''
传入一个字符串，反转内容
'''
def nuberreverse(nub):
    if nub == 0:
        return 0
    str_x = str(nub)
    nub = ""
    nub = str_x[0]
    if str_x[0] == "-":
        nub += "-"
# str[len(str) -1::-1]：字符串[开始点，结束点，步长]，步长为负，从右到左
# lstrip() 方法用于截掉字符串左边的空格或指定字符；rstrip()方法用于截掉字符串右边的空格或指定字符。
    nub = str_x[len(str_x)-1::-1].rstrip("-").lstrip("0")
    nub = int(nub)
    if -2 ** 31 < nub < 2 ** 31 - 1:
        return nub
    return 0

print(nuberreverse(4253))