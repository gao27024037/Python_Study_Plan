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

#
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

# 从备份文件中读入备份数据并写入到记录文件中
def writeBak2Record(bakFile):
    bakFile = file(task+'.bak','r')
    string=bakFile.readline()
    times=string.split(',')
    writeRecord(formatTime(float(times[0]),float(times[1])))
    writeTotalTime(int(float(times[1]) - float(times[0])))

# 把t1,t2时间格式化
def formatTime(startTime, endTime):
    return time.strftime('%Y-%m-%d 星期%w %H:%M:%S', time.localtime(startTime)) + "--->" \
        + time.strftime('%Y-%m-%d 星期%w %H:%M:%S', time.localtime(endTime)) + \
        " 持续：" + min2Time(int(endTime - startTime)) + '\n'

# 保存备份
def saveBak(startTime, bakTime):
    bakFile = file(task + '.bak', 'w')
    bakFile.write(str(startTime)+','+str(bakTime))
    bakFile.close()


if __name__ == '__main__':
    gap = 60
    task = 'SkyrimSE'
    # 存在taskName.txt则读入其中的名字 作为进程名
    if os.path.exists('task_names.txt'):
        fname = file('task_names.txt', 'r')
        task = fname.readline()
    # 循环监控
    while True:
        # 如果存在备份文件，则读入其中的数据并写入记录文件中，后删除备份文件
        if os.path.exists(task+'.bak'):
            writeBak2Record(task+'.bak')
            os.remove(task+'.bak')
        # 若进程存在，则纪录开始时间，否则休眠gap秒
        if check_exsit(task + '.exe'):
            startTime = time.time()
            # 若程序存在，则纪录当前时间，写入备份文件中
            while check_exsit(task + '.exe'):
                time.sleep(gap)
                endTime = time.time()
                saveBak(startTime,endTime)
        else:
            time.sleep(gap)
