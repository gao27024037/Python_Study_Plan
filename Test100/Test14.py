# -*- coding:utf-8 -*- 
# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3
# *3*5。
from math import sqrt
x = int(raw_input('input:'))

l=[]
while x not in [1]:
   for i in xrange(2,x+1):
       if x%i==0:
           x/=i
           l.append(i)
           break
   else:
       l.append(x)

print l