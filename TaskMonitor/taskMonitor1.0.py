# -*- coding:utf-8 -*-
# 编码声明
import win32com.client
import time
import os

task = 'chrome'


# 判断是否存在
def check_exsit(process_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:  # 判断操作 www.iplaypy.com
        print '%s is exists' % process_name
        return True
    else:
        print '%s is not exists' % process_name
        return False

# 秒变为时分
def min2Time(time):
    hour = time / 3600
    minute = (time - hour * 3600) / 60
    second = (time - hour * 3600 - 60 * minute)
    return "%d:%d:%d" % (hour, minute, second)


# 计算总时间
def addTotalTime(t, s='00:00:00'):
    time0 = s.split(':')
    time = [int(i) for i in time0]
    t = t + time[0] * 3600 + time[1] * 60 + time[2]
    return min2Time(t)


# 追加时间轴s
def writeRecord(s):
    frecord = file(task + 'TimeLine.txt', 'a')
    frecord.write(s)
    frecord.close()


def writeTotalTime(t):
    if os.path.exists(task + 'TotalTime.txt'):
        fTotalTime = file(task + 'TotalTime.txt', 'r')
        s = fTotalTime.readline()
        fTotalTime = file(task + 'TotalTime.txt', 'w')
        fTotalTime.write(addTotalTime(t, s))
    else:
        fTotalTime = file(task + 'TotalTime.txt', 'w')
        fTotalTime.write(addTotalTime(t))
    fTotalTime.close()


if __name__ == '__main__':
    gap = 60
    task = 'SkyrimSE'
    if os.path.exists('task_names.txt'):
        fname = file('task_names.txt', 'r')
        task = fname.readline()
    while True:
        if check_exsit(task + '.exe'):
            t1 = time.time()
            while check_exsit(task + '.exe'):
                time.sleep(gap)
            t2 = time.time()
            s = time.strftime('%Y-%m-%d 星期%w %H:%M:%S', time.localtime(t1)) + "--->" \
                + time.strftime('%Y-%m-%d 星期%w %H:%M:%S', time.localtime(t2)) + \
                " 持续：" + min2Time(int(t2 - t1)) + '\n'
            print s
            writeRecord(s)
            writeTotalTime(int(t2 - t1))
        else:
            time.sleep(gap)
