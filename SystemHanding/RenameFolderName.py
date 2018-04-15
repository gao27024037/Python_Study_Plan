# 为兼职文件夹重命名 去掉后面的01

import os
import re

if __name__ == '__main__':
    s=os.listdir(u"D:\part-time job")
    os.chdir(u"D:\part-time job")
    for i in s:
        if re.match('\d',i) is not None:
            print(i[:8])
            os.rename(i,i[:8])
