import wmi
c = wmi.WMI ()
task_list=set()
for process in c.Win32_Process():
    task_list.add(process.Name)
print(task_list)