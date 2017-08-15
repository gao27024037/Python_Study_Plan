# -*- coding:utf-8 -*- 
# 题目：输出 9*9 乘法口诀表。
for i in range(10):
    print '\n'
    for j in range(1,i+1):
        print '%d * %d = %d' % (j,i,i*j),