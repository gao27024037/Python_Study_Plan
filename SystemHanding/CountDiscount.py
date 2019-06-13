# @Time    : 8/7/2018 3:30 PM
# @Author  : GYL
# @File    : CountDiscount.py
# @Description:
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    discount_list=[]
    # for line in open("华为手机助手导出的短信2018-08-07_152142771.csv",encoding='utf-8'):
    for line in open("华为手机助手导出的短信2018-10-29_231233136.csv",encoding='utf-8'):
        if ')，已优惠' in line:
            s = line.split(',')[2]
            n=s.index("已优惠")+3
            num=s[n]+s[n+1]+s[n+2]+s[n+3]
            discount_list.append(float(num))
    print("sum:",sum(discount_list))
    print("size:",len(discount_list))
    print("average",sum(discount_list)/len(discount_list))
    print("max",max(discount_list))
    print("min",min(discount_list))
    data=np.array(discount_list)
    data=data[data<5]
    print(data.shape)
    plt.hist(data,bins=30, width=0.05)
    plt.show()


