# -*- coding:utf-8 -*-

'''
b = x if x>=1 else 1
如果x的值大于等于1， 则将x赋值给b，否则将1赋值给b，这一句等价于
if x>=1:
b =x
else:
b=1
'''
a = [3,4,5]
b = [4,2,6,7]
#4612

def Twowordsum(a,b):
    sum=[]
    la,lb,carry = len(a)-1,len(b)-1,0
    while la >= 0 or lb >= 0:
        x = a[la] if la >= 0 else 0
        y = b[lb] if lb >= 0 else 0
        print(x,y,carry)
        now = x + y + carry
        sum.append(now%10)
        la,lb,carry = la - 1,lb - 1,now//10
    return sum[::-1]

print(TwoWordSum(a,b))