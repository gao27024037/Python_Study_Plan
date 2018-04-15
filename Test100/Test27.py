# -*- coding:utf-8 -*- 
# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出
# 来。
def output(s):
    if len(s) == 1:
        print s
    else:
        output(s[1:])
        output(s[0])
word = raw_input("word:")
output(word)