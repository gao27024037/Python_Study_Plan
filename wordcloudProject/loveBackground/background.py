#create wordcloud for wechat backgroud with my girlfriend:llm
import random

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    if random.random()<0.3:
        data="hsl(%d, %d%%, %d%%)" % (random.randint(200,240),random.randint(0, 10),random.randint(20,60))
    else:
        data="hsl(%d, %d%%, %d%%)" % (random.randint(320,360),random.randint(90, 100),random.randint(70,85))
    return data

def get_word_frequency_dict(filename):
    word_frequency_dict={}
    for i in open(filename,'r',encoding='utf-8'):
        line=i.split(' ')
        if  len(line) is 1 or line[1] == '\n':
            line.append(random.randrange(2,6))
        if int(line[1])>10:
            line[1]=10
        word_frequency_dict[line[0]]=int(line[1])
    return word_frequency_dict


def creat_word_cloud(word_frequency_dict,name):
    word_cloud=WordCloud( background_color="white", #背景颜色
                          width=540, height=960, margin=2,
                          prefer_horizontal=1,
                            max_words=1800,# 词云显示的最大词数
                            max_font_size=60, #字体最大值
                            min_font_size=20,
                            font_path='simkai.ttf',
                            random_state=40,
                          color_func=grey_color_func
                          ).generate_from_frequencies(word_frequency_dict)

    word_cloud.to_file(name+".jpg")
    plt.imshow(word_cloud)
    plt.axis("off")


if __name__ == '__main__':
    print("**********************许多句话背景图片*************************")
    print()
    print("*           感谢使用**许多句话背景图片**制作工具")
    print("*           制作人：大宝贝&小宝贝 —— G ❤ L  ヾ(≧▽≦*)o")
    print("*")
    print("*   TXT文件格式要求：1.每行一句话")
    print("*                    2.话后隔一空格加数字（不大于10）,代表该句话在图中大小")
    print("*                    3.数字也可不加，表示大小随机")
    print("*   源码参考地址：https://github.com/gao27024037/Python_Study_Plan/tree/master/wordcloudProject/loveBackground")
    print("***************************************************************")
    print('\n')

    file = input("请输入txt文件地址：")
    jpg = input('请输入输出图片名字：')
    while True:
        creat_word_cloud(get_word_frequency_dict(file),jpg)
        print("\n图片已生成："+jpg+".jpg ,如不满意请按N重新生成，如满意请按Y退出程序。")
        answer = input('满意吗？（Y/N）')
        if answer == 'y' or answer == 'Y':
            exit()
