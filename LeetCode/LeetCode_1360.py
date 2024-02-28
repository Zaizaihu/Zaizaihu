# -*- coding:utf-8 -*-
'''请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。'''

#   闰年 + 1
#   日期格式：1991 - 1 - 2
#   MM & DD 是否大于12 & 31
class Solution:
    def date_to_int(self, year, month, day):

        #判断时间是否在 1971 到 2100 之间
        if year < 1971 or year > 2100:
            return "您输入的时间有误"
        month_length = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        ans = int(year / 4) + year * 365  #计算闰年
        ans = ans + month_length[month - 1]  #按月累加时间
        ans = ans + day
        return ans

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = [int(i) for i in date1.split('-')]
        date2 = [int(i) for i in date2.split('-')]
        print(self.date_to_int(*date1),self.date_to_int(*date2),type(self.date_to_int(*date1)))
        if isinstance(self.date_to_int(*date1),int) and isinstance(self.date_to_int(*date2),int) :
            return print("日期之间相隔",abs(self.date_to_int(* date1) - self.date_to_int(* date2)),"天")

        else:
            return print("您输入的时间有误--date2")



Solution().daysBetweenDates("1992-2-4","1992-4-2")

