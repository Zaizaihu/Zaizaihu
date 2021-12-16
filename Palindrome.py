# -*- coding:utf-8 -*-

def Palindrome(nuber):
    if nuber == 0:
        return 0
    Pnuber = str(nuber)
    othernuber = Pnuber[len(Pnuber)-1::-1]
    if Pnuber == othernuber:
        return print("true")
    else:
        print("false")

Palindrome("-14141-")
