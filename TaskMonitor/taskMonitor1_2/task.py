import os
import time


class Task(object):
    start_time =0
    end_time = 0

    def __init__(self, name):
        self.name = name
        if os.path.exists(self.name + '.bak'):
            self.write_bak_to_record()
            os.remove(self.name + '.bak')


    #检查
    def check(self, task_list):
        if self.name+'.exe' in task_list:
            if self.start_time==0:
                self.start_time=time.time()
            else :
                self.end_time=time.time()
                self.save_bak()
            print(self.name+" exist")
        else:
            if  self.start_time!=0:
                if os.path.exists(self.name + '.bak'):
                    self.write_bak_to_record()
                    os.remove(self.name + '.bak')
                self.start_time=0
            print(self.name+" is not exist")



        # 从备份文件中读入备份数据并写入到记录文件中
    def write_bak_to_record(self):
        bak_file = open(self.name + '.bak', 'r')
        string = bak_file.readline()
        times = string.split(',')
        self.write_record(self.format_time(float(times[0]), float(times[1])))
        self.write_total_time(int(float(times[1]) - float(times[0])))

    # 追加时间轴s
    def write_record(self,s):
        file_record = open(self.name + '_time_line.txt', 'a', encoding='utf-8')
        file_record.write(s)
        file_record.close()

    # 把t1,t2时间格式化
    def format_time(self, start_time, end_time):
        return time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(start_time)) + "--->" \
               + time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(end_time)) + \
               " Lasted: " + self.min_to_time(int(end_time - start_time)) + '\n'

    def min_to_time(self, time):
        hour = time // 3600
        minute = (time - hour * 3600) // 60
        second = (time - hour * 3600 - 60 * minute)
        return "%d:%d:%d" % (hour, minute, second)

    #写入总时间
    def write_total_time(self,total_time):
        str="_total_time"
        if os.path.exists(self.name + str+'.txt'):
            file_total_time = open(self.name +str+'.txt', 'r')
            s = file_total_time.readline()
            file_total_time = open(self.name + str+ '.txt', 'w')
            file_total_time.write(self.add_total_time(total_time, s))
        else:
            file_total_time = open(self.name + str +'.txt', 'w')
            file_total_time.write(self.add_total_time(total_time))
        file_total_time.close()


    # 计算总时间
    def add_total_time(self, total_time, s='00:00:00'):
        time0 = s.split(':')
        time = [int(i) for i in time0]
        total_time = total_time + time[0] * 3600 + time[1] * 60 + time[2]
        return self.min_to_time(total_time)

    def save_bak(self):
        bak_file=open(self.name+'.bak','w')
        bak_file.write(str(self.start_time)+','+str(self.end_time))
        bak_file.close()


