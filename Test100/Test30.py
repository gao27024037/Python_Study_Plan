# -*- coding:utf-8 -*- 
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位
# 与万位相同，十位与千位相同。
def isReserve(num):
    s = str(num)
    for i in range(len(s)):
        if s[i]!=s[-i-1]:
            return False
    return True

print isReserve(123210)