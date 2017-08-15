# -*- coding:utf-8 -*- 
# 题目：斐波那契数列。

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print a,


fib(int(raw_input('numbers:\n')))
