# coding=utf-8
import os
import re

if __name__ == '__main__':
    s = os.listdir(u"G:/迅雷下载")
    os.chdir(u"G:/迅雷下载/")
    for i in s:
        print i
        a = re.search('S04E\d+',i)          #正则匹配
        if a is not None:
            print a.group()
            os.rename(i,'Agents of SHIELD'+a.group()+'.mkv')