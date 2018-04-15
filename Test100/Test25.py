# -*- coding:utf-8 -*- 
# 题目：求1+2!+3!+...+20!的和。
def sumFactorial(n):
	num=1
	s=num
	for i in range(1,n):
		num=num*(i+1)
		s+=num
	return s
print sumFactorial(20)