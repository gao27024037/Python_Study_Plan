# http://www.runoob.com/python/python-100-examples.html
# -*- coding:utf-8 -*-
import urllib2
import gzip
import StringIO
from bs4 import BeautifulSoup

url0 = 'http://www.runoob.com/python/python-exercise-example'
failed=[]
for j in range(1, 101):

# 爬数据
    url = url0 + str(j) + '.html'
    headers = {'Accept-encoding': 'gzip'}
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    Encode = urllib2.urlopen(request).info().get('Content-Encoding')
    if Encode == 'gzip':
        html = gzip.GzipFile(fileobj=StringIO.StringIO(html), mode="r").read()
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    question = soup.find('strong').parent

# 写数据
    try:
        f = file("Test" + str(j) + ".py", 'w')
        f.write('# -*- coding:utf-8 -*- ')
        question = list('\n# '+question.get_text())
        for i in range(1, len(question) / 35):
            question.insert(i * 35, '\n# ')
        f.write("".join(question).encode('utf-8'))
        print 'write data success', j
    except:
        print 'write data failed', j
        failed.append(j)

print failed
