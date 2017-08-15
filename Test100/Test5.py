# -*- coding:utf-8 -*- 
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
x,y,z=int(raw_input('x: ')),int(raw_input('y: ')),int(raw_input('z: '))
arr = [x,y,z]
arr.sort()
print arr