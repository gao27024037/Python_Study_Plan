# -*- coding:utf-8 -*- 
# 题目：打印出如下图案（菱形）:
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *

lenth=7
for i in range(1,lenth+1):
        print " "*abs(lenth/2+1-i)+'*'*(lenth-2*abs(lenth/2+1-i))+" "*abs(lenth/2+1-i)


