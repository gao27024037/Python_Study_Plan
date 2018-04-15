# -*- coding:utf-8 -*-
#python2

import requests
import jieba
import codecs
import re
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread
from PIL import Image

def get_html(url):
    r = requests.get(url)
    # print r.status_code
    return r.text


# 获取每篇文章url
def get_article_url():
    article_url_set = set([])
    string = '?order_by=shared_at&page='
    for page in range(1, 6):
        url = 'http://www.jianshu.com/u/b0ad48517581' + string + str(page)
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all('a', 'title')
        for a in tags:
            if re.match('/u/', a['href']) is None:
                article_url_set.add(a['href'])
    return article_url_set


# 获取文章
def get_article(article_url):
    # article_url = 'http://www.jianshu.com/p/48cad157f604'
    # print article_url
    article_html = get_html(article_url)
    page_soup = BeautifulSoup(article_html, 'html.parser')
    content = page_soup.find('div', 'show-content')
    article = content.get_text().replace('图片发自简书App'.decode('utf8'), '')  # 拿到文章内容s
    return article


# 计算词频
def get_word_frequency(article_url_set):
    word_frequency_dict = {}
    for article_url in article_url_set:
        print 'reading http://www.jianshu.com' + article_url
        article = get_article('http://www.jianshu.com' + article_url)  # 获取文章内容
        words = jieba.cut(article)  # 分词
        for word in words:  # 统计词频
            if ((re.match(u'([\u4e00-\u9fa5]|\w)+', word)) is not None) and (word not in stop_word):
                if word_frequency_dict.has_key(word):
                    word_frequency_dict[word] = word_frequency_dict.get(word) + 1
                else:
                    word_frequency_dict[word] = 1
    return word_frequency_dict


# 获取停用词
def get_stop_words(filename):
    stop_word = ([])
    f = codecs.open(filename, 'r', 'utf-8')
    for word in f.readlines():
        stop_word.append(re.match(u'([\u4e00-\u9fa5])+', word).group())
    return stop_word


def creat_word_cloud(word_frequency_dict):
    pic = np.array(Image.open("pic.jpg"))
    word_cloud=WordCloud( background_color="white", #背景颜色
                max_words=1800,# 词云显示的最大词数
                mask=pic,#设置背景图片
                max_font_size=180, #字体最大值
                random_state=40,
                color_func=ImageColorGenerator(pic)
                ).generate_from_frequencies(word_frequency_dict)
    word_cloud.to_file("pjl_cloud.jpg")
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    stop_word = get_stop_words('stopword.txt')
    article_url_set = get_article_url()
    word_frequency_dict = get_word_frequency(article_url_set)
    f=file('jianshu.txt','a')
    for k,v in word_frequency_dict.items():
        s = k+' '+str(v)+'\n'
        f.write(s.encode('utf-8'))
    creat_word_cloud(word_frequency_dict)
