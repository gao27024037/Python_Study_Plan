# -*- coding:utf-8 -*- 
# 题目：利用递归方法求5!。
def factorial(n):
	if n == 1:
		return 1
	else:
		return  n*factorial(n-1)
print factorial(5)