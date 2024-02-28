# -*- coding:utf-8 -*-
'''
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
'''

class Solution():
    def return_last_word(self,word:str):
        result = word.split()
        return result[-1]

word = "luffy is still joyboy"
print(Solution().return_last_word(word))
