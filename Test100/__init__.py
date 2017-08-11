# http://www.runoob.com/python/python-100-examples.html
# -*- coding:utf-8 -*-
import urllib2
import gzip
import StringIO
from bs4 import BeautifulSoup
url0 = 'http://www.runoob.com/python/python-exercise-example'
for j in range(1, 101):

    url = url0+str(j)+'.html'
    print url
    response = urllib2.urlopen(url)
    #print response.getcode()
    # cont = response.read()
    # 网页采用了gzip压缩
    # cont = StringIO.StringIO(response.read())
    # gzipper = gzip.GzipFile(fileobj=StringIO.StringIO(response.read()))
    try:
        context = gzip.GzipFile(fileobj=StringIO.StringIO(response.read())).read()
        print 'get data success',j
    except:
        print 'get data failed',j
        context = response.read()
    soup = BeautifulSoup(context, 'html.parser', from_encoding='utf-8')
    question = soup.find('strong').parent

    try:
        f = file("Test" + str(j) + ".py", 'w')
        f.write('# -*- coding:utf-8 -*-')
        f.write('\n#' + question.get_text().encode('utf-8'))
        print 'write data success',j
    except:
        print 'write data failed',j

