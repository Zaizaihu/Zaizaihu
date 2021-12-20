# -*- coding:utf-8 -*-

# Bite = input()
# def Rebite(s):
#     a = []
#     xb=1
#     for i in s:
#         a.append(s[-xb])
#         xb += 1
#     return print(a)


def Rebite(s):
    print(s)
    if s =="":
        print(s)
        return s
    else:
        return Rebite(s[1:])+s[0]

if __name__ == '__main__':
    print(Rebite("hujingwang"))