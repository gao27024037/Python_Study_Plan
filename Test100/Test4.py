# -*- coding:utf-8 -*- 
# 题目：输入某年某月某日，判断这一天是这一年的第几天？

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if 0<month<=12 and 0<day<=31:
    sum=months[month-1]+day
else:
    print 'data error'
if year%400==0 or (year%4==0 and year%100!=0):
    if month>2:
        sum +=1

print 'it is the %dth day in the year .'%sum