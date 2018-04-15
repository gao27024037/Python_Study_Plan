# coding=utf-8
# 简化神盾局特工每一剧集的名字，去掉.和无用单词，便于迅雷影音匹配字幕

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
            os.rename(i,'Agents of SHIELD '+a.group()+'.mkv')