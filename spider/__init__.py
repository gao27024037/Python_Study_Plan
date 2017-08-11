# -*- coding:utf-8 -*-
import urllib2
import gzip
import StringIO
from bs4 import BeautifulSoup

url2 = 'http://www.runoob.com/python/python-exercise-example3.html'
response = urllib2.urlopen(url2)
#print response.getcode()
# cont = response.read()
# 网页采用了gzip压缩
# cont = StringIO.StringIO(response.read())
# gzipper = gzip.GzipFile(fileobj=StringIO.StringIO(response.read()))
# context = gzip.GzipFile(fileobj=StringIO.StringIO(response.read())).read()
context = response.read()
soup = BeautifulSoup(context, 'html.parser', from_encoding='utf-8')
question = soup.find('strong').parent
print question.get_text()

