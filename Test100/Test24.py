# -*- coding:utf-8 -*- 
# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，2
# 1/13...求出这个数列的前20项之和。
def cal(n):
	a,b=2.0,3.0
	x,y=1.0,2.0
	s=0.0
	for i in range(n):
		s = s + a/x
		a,b=b,a+b
		x,y=y,x+y
	return s
print cal(20)	
