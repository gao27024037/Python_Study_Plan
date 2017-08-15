# -*- coding:utf-8 -*- 
# 题目：判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt
l=[]
for i in range(101,201):
    for n in range(2,int(sqrt(i))+1):
        if i%n==0:
            break
    else:
        l.append(i)
print l
