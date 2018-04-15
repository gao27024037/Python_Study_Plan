# -*- coding:utf-8 -*- 
# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序
# 打印出各位数字。
# from Test27 import output
def digits(num):
    if (num / 10) >0:
        return digits(num/10) + 1
    else:
        return 1

def output(s):
    if len(s) == 1:
        return s
    else:
        return output(s[1:])+output(s[0])
num = int(raw_input("num:"))
print digits(num), output(str(num))
