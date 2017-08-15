# -*- coding:utf-8 -*- 
# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a
# 是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。
x=int(raw_input('number:\n'))
s=num=x
for n in range(5):
    num=int(str(num)+str(x))
    s+=num
    print num
print s