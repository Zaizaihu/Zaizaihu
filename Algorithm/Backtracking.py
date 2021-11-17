# -*- coding:utf-8 -*-
'''
leetcode：22         回溯算法
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
“((()))”,
“(()())”,
“(())()”,
“()(())”,
“()()()”
]
1、左括号不能呢大于N
2、右括号不能大于左括号

'''
def baidu(n):
    ans=[]
    def backtracking(S,left,right):
        if len(S) == 2*n:
            ans.append(''.join(S))
            return
        if left < n:
            S.append("(")
            backtracking(S,left+1,right)
            S.pop()
        if right < left:
            S.append(")")
            backtracking(S,left,right+1)
            S.pop()
    backtracking([],0,0)
    return ans

print(baidu(3))