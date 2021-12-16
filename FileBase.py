# -*- coding:utf-8 -*-
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

if __name__ == '__main__':
    # read_file("hjw.txt")
    copy_file("hjw.txt","Data.txt")