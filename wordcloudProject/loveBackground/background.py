#create wordcloud for wechat backgroud with my girlfriend:llm
print("加载数据包中，请耐心等待。。")
import random
import wordcloud
import matplotlib.pyplot as plt
from click._compat import raw_input
import os
import chardet
import codecs


import numpy
import PIL
import colorsys
import matplotlib
import builtins

#转化文本文件为utf-8 如果不是 重新输入
def convert_to_utf8(filename):
    try:
        content=open(filename,'rb').read()
        ecode=chardet.detect(content)['encoding']
        if  ecode[:2]=='GB':
            ecode='GBK'
        str=content.decode(encoding=ecode).encode(encoding='utf-8')
        open(filename,'w',encoding='utf-8').write(str.decode(encoding='utf-8'))
        return True
    except:
        return False

#获取颜色
def color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    if random.random()<0.3:
        data="hsl(%d, %d%%, %d%%)" % (random.randint(200,240),random.randint(0, 10),random.randint(20,60))
    else:
        data="hsl(%d, %d%%, %d%%)" % (random.randint(320,360),random.randint(90, 100),random.randint(70,85))
    return data

#获取词频
def get_word_frequency_dict(filename):
    while convert_to_utf8(filename) is False:
        file = raw_input(file+"文件格式错误，请重新输入正确的文本格式（含文件后缀,如：input.txt）：")
    word_frequency_dict={}
    file=open(filename, 'r',encoding='utf-8')
    for i in file:
        line=i.split(' ')
        if  len(line) is 1 or line[1] == '\n':
            line.append(random.randrange(3,6))
        if int(line[1])>10:
            line[1]=10
        word_frequency_dict[line[0]]=int(line[1])
    return word_frequency_dict


def creat_word_cloud(word_frequency_dict,name):
    word_cloud=wordcloud.WordCloud( background_color="white", #背景颜色
                          width=400, height=600, margin=2,
                          prefer_horizontal=1,
                            max_words=1800,# 词云显示的最大词数
                            max_font_size=40, #字体最大值
                            min_font_size=5,
                            font_path='simkai.ttf',
                            random_state=40,
                          color_func=color_func
                          ).generate_from_frequencies(word_frequency_dict)

    word_cloud.to_file(name+".jpg")
    plt.imshow(word_cloud)
    plt.axis("off")

def print_title():
    print("**********************文字背景壁纸*************************")
    print("*")
    print("*           感谢使用**文字背景壁纸**制作工具")
    print("*           制作人：大宝贝&小宝贝 —— G ❤ L  ヾ(≧▽≦*)o")
    print("*")
    print("*   TXT文件格式要求：1.每行一句话,一共20行左右为宜")
    print("*                    2.话后隔一空格加数字（不大于10）,代表该句话在图中大小")
    print("*                    3.数字也可不加，表示大小随机")
    print("*   如有疑问，请联系原作者：github--gao27024037")
    print("*   源码参考地址：https://github.com/gao27024037/Python_Study_Plan/tree/master/wordcloudProject/loveBackground")
    print("***************************************************************")
    print('\n')


if __name__ == '__main__':
    os.system("cls")
    print_title()

    #检测文件
    file = raw_input("请输入txt文件地址（含文件后缀,如：input.txt）：")
    while os.path.exists(file) is False:
        file = raw_input(file+"文件不存在，请重新输入txt文件地址（含文件后缀,如：input.txt）：")
    while convert_to_utf8(file) is False:
        file = raw_input(file+"文件格式错误，请重新输入正确的文本格式（含文件后缀,如：input.txt）：")
    jpg = raw_input('请输入输出图片名字(不含后缀，如： output)：')

    while True:
        creat_word_cloud(get_word_frequency_dict(file),jpg)
        print("\n图片已生成："+jpg+".jpg ,如不满意请按N重新生成，如满意请按Y退出程序。")
        answer = raw_input('满意吗？（Y/N）')
        if answer == 'y' or answer == 'Y':
            exit(0)

