import wmi
import time

from TaskMonitor.taskMonitor1_2.task import Task

if __name__ == '__main__':
    monitor_list=[]
    while(1):
        c = wmi.WMI()
        running_task_list = set()
        for process in c.Win32_Process():
            running_task_list.add(process.Name)
        # 存在taskName.txt则读入其中的名字 作为进程名
        new_list=[]
        for line in open('task_names.txt', 'r'):
            new_list.append(line.split('\n')[0])
        if monitor_list != new_list:
            print("changed")
            monitor_list = new_list.copy()
            tasks=[]
            for task in monitor_list:
                tasks.append(Task(task))
        for task in tasks:
            task.check(running_task_list)
        time.sleep(60)




