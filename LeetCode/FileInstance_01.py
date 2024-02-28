# -*- coding:utf-8 -*-
import FileBase as File
def fils(path):
    index = []
    file = open(path,"r")
    # for i in file:
    #     index.append(i)
    for i in range(File.get_row(path)):
        index.append(File.get_line(path,i))
    print(index)

def merge_file(pathA,pathB):
    pathC = "merged.txt"
    Defeil = open(pathC,"r+")
    File.copy_file(pathA,pathC)
    txtb = open(pathB)
    for i in txtb:
        if i in pathA:
            continue
        else:
            Defeil.line_buffering
            Defeil.write(i + "\n")

def merge_file(pathA):
    File = open(pathA,"r+")
    File.writable()
    File.writelines("bubiu")
    File.close()
if __name__ == '__main__':
    # fils("Data.txt")
    # 追加文件
    merge_file("hjw.txt")