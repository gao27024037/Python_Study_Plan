# -*- coding:utf-8 -*- 
# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如
# 6=1＋2＋3.编程找出1000以内的所有完数。
for x in range(2,1001):
    l = []
    for i in range(1,x):
        if x % i ==0:
            l.append(i)
    if sum(l) == x:
        print x,l
