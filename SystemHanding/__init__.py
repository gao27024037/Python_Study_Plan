# coding=utf-8
import re

import jieba

from spider.jianshu import getArticle, getStopWord

article_url = 'http://www.jianshu.com/p/48cad157f604'
article = getArticle(article_url)  # 获取文章内容
words = jieba.cut(article)  # 分词
stop_word = getStopWord('D:\Code\python\Python_Study_Plan\spider\stopword.txt')
word_frequency_dict = {}
for word in words:  # 统计词频
    if word in stop_word:
        if word_frequency_dict.has_key(word):
            word_frequency_dict[word] = word_frequency_dict.get(word) + 1
        else:
            word_frequency_dict[word] = 1
for word in word_frequency_dict:
    print word,