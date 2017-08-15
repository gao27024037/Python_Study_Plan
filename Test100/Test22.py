# -*- coding:utf-8 -*- 
# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队
# 为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说
# 他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

a, b, c = 0,1, 2
for x in set(range(3)):
    for y in set(range(3)) - set([x]):
        for z in set(range(3)) - set([x, y]):
            if a != x and c == y:
                print x, y, z
