# -*- coding:utf-8 -*-
import openpyxl
import xlwt

def read_file(path):
    file = open(path,"r")
    fullfile = file.readlines()
    file.close()
    return fullfile

    #遍历前五行
    # for i  in range(5):
    #     line = file.readline()
    #     print(line[:-1])

    #遍历文件
    # for i in file:
    #     print(i)

def get_row(path):
    file = open(path,"r")
    row = len(file.readlines())
    return row


def get_line(path,index):
    file = open(path, "r")
    for i  in range(index):
        line = file.readline()
        return line


def copy_file(path1,path2):
    f1 = open(path1,"r+")
    f2 = open(path2,"r+")
    countLine =  0
    for i  in f1:
        countLine += 1
        f2.writelines(i)
    f1.close()
    f2.close()

def creat_excle(name):
    workbook = xlwt.Workbook(encoding='utf-8')
    # 使用add_sheet()方法，在新建的工作簿上新增sheet页
    sheet1 = workbook.add_sheet(name)
    # 将新增的Excel文件存储于指定地址中
    workbook.save(r"/Users/wangzai/PycharmProjects/ZaiFirst/LeetCode/%s.xlsx"%name)



if __name__ == '__main__':
    # read_file("hjw.txt")
    # creat_excle("杭州搜车网科技有限公司")
    pass