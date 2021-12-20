# -*- coding:utf-8 -*-
"""罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

IV(5) 和X(10) 的左边，来表示 4 和 9。
XL(50) 和C(100) 的左边，来表示 40 和90。
CD(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

解题思路
1、输入Romannuber
2、处理过程
新建罗马数组转数字的字典
将Romannuber转为字符串，循环遍历（少一轮，最后一轮在循环外直接加）当前字符的映射值是否大于上个字符，是为"负数"，否为正数。由nuber累加
3、返回nuber

解法2
1、输入Romannuber
2、处理过程
新建罗马数组转数字的字典与特殊字典。特殊字典存放特殊内容如IV=4
将Romannuber转为字符串，循环遍历（少一轮，最后一轮在循环外直接加）,取两位数查看是否在特殊字典中，是第一位为"负数"，否第一位为正数。由nuber累加第一位
3、返回nuber"""
def Romannuber(Roman):
    romannabers = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000,"IV": 4,"IX": 9,"XL": 40,"XC": 90,"CD": 500,"CM":900}
    strR = str(Roman)
    nuber = 0
    for i in range(len(strR)-1):
        print(nuber)
        if romannabers[strR[i]] < romannabers[strR[i+1]]:
            nuber -= romannabers[strR[i]]
            print("当前数大于上个字符s%",romannabers[strR[i]])
        else:
            nuber += romannabers[strR[i]]
            print("当前数小于上个字符为%s",romannabers[strR[i]])
    nuber += romannabers[strR[-1]]
    return nuber

print(Romannuber("V"))