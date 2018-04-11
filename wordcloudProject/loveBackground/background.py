#create wordcloud for wechat backgroud with my girlfriend
import random

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    if random.random()<0.3:
        data="hsl(%d, %d%%, %d%%)" % (random.randint(150,240),random.randint(50, 70),random.randint(0,60))
    else:
        data="hsl(%d, %d%%, %d%%)" % (random.randint(270,360),random.randint(80, 100),random.randint(50, 80))
    print(data)
    return data

def get_word_frequency_dict(filename):
    word_frequency_dict={}
    for i in open(filename,'r',encoding='utf-8'):
        line=i.split(' ')
        if  len(line) is 1:
            line.append(random.randrange(2,6))
        word_frequency_dict[line[0]]=int(line[1])
    return word_frequency_dict


def creat_word_cloud(word_frequency_dict):
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

    word_cloud.to_file("girlfriend.jpg")
    plt.imshow(word_cloud)
    plt.axis("off")


if __name__ == '__main__':

    creat_word_cloud(get_word_frequency_dict('girlfriend.txt'))