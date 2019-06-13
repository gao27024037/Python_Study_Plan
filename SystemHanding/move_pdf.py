# 移动pdf文件到D:\graduate\Papers\myPapers

import os
import time
import subprocess

def deal_file(file):
    cmd = 'move "'+str(file)+'" "'+str(destination + file)+'"'
    print(cmd)
    p=subprocess.run(cmd,shell=True,stdout=subprocess.PIPE)
    print(p.stdout)
    if  b"1 file(s) moved." in p.stdout:
        log_file = open(log_path + "move_pdf.log", 'a', encoding='utf8')
        log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(log_time + " move " + file + " from " + source + " to " + destination + "\n")
        log_file.close()

if __name__ == '__main__':
    conf = open("move_pdf.conf", "r", encoding="utf8")
    source = None
    destination = None
    scan_time = 30
    for line in conf:
        if 'source' in line:
            source = line.strip().split("=")[1]
        elif 'destination' in line:
            destination = line.strip().split("=")[1]
        elif 'scan_time' in line:
            scan_time = (int)(line.strip().split("=")[1])
    print(source, destination)
    log_path = destination
    os.chdir(source)
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        s = os.listdir(source)
        for file in s:
            if ".pdf" == file[-4:]:
                deal_file(file)
        time.sleep(scan_time)
