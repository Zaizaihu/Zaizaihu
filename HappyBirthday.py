# -*- coding:utf-8 -*-



def happy(name=None):
    if name== None:
        print("happy Brithdat to you")
    else:
        print("happy Brithdat to dear" + " " + name)

def toYou():
    name = input("请输入你的名字,如果有多个用空格分割").split()
    for i in name:
        happy()
        happy()
        happy(i)
        happy()

if __name__ == '__main__':
    toYou()