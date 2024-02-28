# -*- coding:utf-8 -*-
'''数据类型：
不可变数据（3 个）：Number（数字1234）、String（字符串hujingwang）、Tuple（元组（））；
可变数据（3 个）：List（列表[]）、Dictionary（字典(a:b,b:c)）、Set（集合{}）。
'''
import datetime

# 字符串：有序，不可变
Str = "hujingwangjingjing"
Str_1 = "1 2 3 4"
Str_2 = "hjw ll hjw wxy zr xq sls msr"


# # 添加内容
# #+
# AS = Str + Str_1
# # 添加内容
# # join
# AS_1 = Str.join(Str_1)
# print(AS_1)

# #替换内容
# #replace
# AS_2 = Str.replace("jing","")
# print(AS_2)
# #指定替换前x个内容
# AS_2 = Str.replace("jing","",2)
# print(AS_2)
# # 查找内容，返回下标
# #find
# print(Str.find("wangjing"))
# # [] 切片 【其实位置，结束位置，间隔】
# print(Str[::2])


# list
List = [14,23,54,"efjisn",'32',42]
# 添加内容
# +
# List = List + [18,]
# print(List)
#
# append：
# List.append([2,"32"])
#
# inserd
# List.insert(3,"nihao")
# print(List)
#
# extend 将内容当作list添加：
# List.extend("huje")
# List.extend([32,43,"je"])
# print(List)
#
# 通过索引删除指定位置元素
# del：
# del List[0]
# print(List)
#
# pop：   //默认删除最后一位
# List.pop()
# print(List)
#
# 移除表中指定值的第一个匹配值，如果找不到，抛异常
# remove：
# List.remove(54)
# print(List)
#
# #修改内容
# List[4] = "hjw"
# print(List)


# 字典 ：有序，可变
ainfo = {"a":1 ,"name":"hujingwang","hjw":["hej",13]}
binfo = dict(a=1)
# #增加与修改内容：
# ainfo["b"] = 2
# print(ainfo,binfo)
#
# #update
# binfo.update(b = 2,c =3)
# print(ainfo,binfo)
#
# 读取Key，value
# for i in ainfo.keys():
#     print(i,ainfo[i])
#
# #删除内容
# ainfo.pop("a")
# print(ainfo)
#
# binfo.clear()
# print(binfo)
#
# del ainfo["b"]
# print(ainfo)


# 元组 ：有序，不可变。可查
b = ("a","b","c",1,2,3,45,1)
# print(b[2])

# # 集合:无序，过滤重复内容
a = {"asbdabcd",32,"ni"}
b = [1,2,3,4,1,3]
c = set("ninosf")

# 添加内容
# a.add(43)
# print(a)
#
# a.update({"44",43,"hje"})
# print(a)
# 删除内容
# a.remove(32)
# a.clear()
# print(a)
from datetime import date
print(date.today())

