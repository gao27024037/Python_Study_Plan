# -*- coding:utf-8 -*- 
# 题目：暂停一秒输出。
import time

mydict = {1:'a',2:'b'}
for k,v in mydict.iteritems():
    print k,v
    time.sleep(1)