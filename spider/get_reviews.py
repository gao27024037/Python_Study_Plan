# python3 爬取大众点评，携程，驴妈妈 关于某一个商家(歌斐颂巧克力小镇)的评论信息
import json
import re
import requests
from bs4 import BeautifulSoup



def get_html(url):
    headers = {'content-type': 'text/html;charset=UTF-8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
               }
    r = requests.get(url,headers=headers)
    print (r.status_code)
    return r.text

def write2file(review_list,s):
    f=open(s+'.csv','a',encoding='utf-8')
    for i in review_list:
        string=''
        for j in i:
            string+=str(j)+','
        string+='\n'
        f.write(string)
        print(string)

def remove_more_space(string):
    return  ' '.join(string.split()).replace("\n"," ").replace("收起评论","").replace(",","，")

# 获取大众点评 评论
def get_reviews_from_dianping(page_soup,article_url,s):
    reviews_items = page_soup.find_all('div', 'main-review')
    review_list=[]
    for i in reviews_items:
        name=remove_more_space(i.find('a','name').get_text())
        score=re.search('\d+',str(i.find('div','review-rank'))).group()
        review_word=remove_more_space(i.find('div',class_=re.compile("review-words")).get_text())
        time=remove_more_space(i.find('span',class_='time').get_text())
        reviews_item=[name,score,review_word,time]
        review_list.append(reviews_item)
    write2file(review_list,s)

#获取驴妈妈评论
def get_reviews_from_lvmama(page_soup, s):
    reviews_items = page_soup.find_all('div', 'comment-li')
    review_list = []
    for i in reviews_items:
        name=i.find('div','com-userinfo').find('p').find('a').get_text()
        score=0
        if i.find('span','ufeed-level'):
            score=re.search('\d+',str(i.find('span','ufeed-level'))).group()
        popularity=re.search('\d+',str(i.find(text=re.compile("人气")).find_next('i'))).group()
        size=re.search('\d+',str(i.find(text=re.compile("规模")).find_next('i'))).group()
        sight=re.search('\d+',str(i.find(text=re.compile("观光")).find_next('i'))).group()
        service=re.search('\d+',str(i.find(text=re.compile("服务")).find_next('i'))).group()
        time=i.find('div','com-userinfo').find('p').find('em').get_text()
        review_word=remove_more_space(i.find('div','ufeed-content').get_text())
        reviews_item=[name,score,popularity,size,sight,service,review_word,time]
        review_list.append(reviews_item)
    write2file(review_list,s)

#携程 3个分数
def get3items_score(i):
    if i.find('span',"sblockline"):
        string=i.find('span',"sblockline").get_text()
        return re.compile('\d+').findall(string)
    else:
        return 0,0,0

#获取携程评论
def get_reviews_from_xiecheng(page_soup, s):
    reviews_items = page_soup.find_all('div',"comment_single")
    review_list = []
    for i in reviews_items:
        name = i.find('a', itemprop="author").get_text()
        score = re.search('\d+', str(i.find('span', "starlist").find("span"))).group()
        sight,interest,cost_effective=get3items_score(i)
        review_word=remove_more_space(i.find("span","heightbox").get_text())
        time = i.find('span',"time_line").find('em').get_text()
        reviews_item = [name, score, sight,interest,cost_effective, review_word, time]
        review_list.append(reviews_item)
    write2file(review_list, s)

#向驴妈妈post的数据
def lvmama_post_data():
    data={"type":"all",
          "currentPage":page,
          "totalCount":"411",
          "placeId":"10000584",
          "productId":"",
          "placeIdType":"PLACE",
          "isPicture":"",
          "isBest":"",
          "isPOI":"Y",
          "isELong":"N"
          }
    return data

#向驴妈妈post的header
def lvmama_post_header():
    headers={'Accept':'text/html, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en,zh-CN;q=0.9,zh;q=0.8',
            'Connection':'keep-alive',
            'Content-Length':'121',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'uid=rBQOcVqgtvt2EmwgD2YdAg==; lvsessionid=04c04486-030f-4588-a478-f0b5e12ac8cd_13799134; cmTPSet=Y; CoreID6=59113046601415204822800&ci=52710000|PC; _ga=GA1.2.461798203.1520482280; _gid=GA1.2.1732399949.1520482280; _jzqc=1; _jzqckmp=1; Hm_lvt_cb09ebb4692b521604e77f4bf0a61013=1520482281; _qzjc=1; _fmdata=3%2FmmlarxQF2K3%2FIT%2BaZRd0xHcUFqZeHEW1I%2FdV5FgupFEx36SGhADqp0oqs7%2FHeQBSt7r8pDnixBAj2Jk7WDj1nsBZHyC7DF0JMqCuCAwM4%3D; fp_ver=4.5.1; BSFIT_EXPIRATION=1521265141567; BSFIT_OkLJUJ=FFFpsggX6iNoR8syzb2HoWhdYRPCaaKA; BSFIT_DEVICEID=jBhadzOVSlDhCx1t6-pMQ2k3zTWBWSNzuImnl9SDCnQ5Hi34Wq8DEJFNalTfIfYrmn5sa4iLZhL8Ikp2CAWJSxZEup-pifYHKLi8y2raUfQx7m4rYUESIbcwBhAXhodOTMNXOZmcYAv1JVitGhjAjVp5ynOB36CM; _pzfxuvpc=1520482280469%7C9542591271666506908%7C2%7C1520484211223%7C2%7C9631739867114428706%7C9399668291532200680; _jzqa=1.3158811549096955000.1520482281.1520482281.1520484211.2; _qzja=1.1132731043.1520482281413.1520482281413.1520484211242.1520482281413.1520484211242..0.0.2.2; _qzjto=2.2.0; __utma=1.461798203.1520482280.1520484212.1520484212.1; __utmc=1; __utmz=1.1520484212.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_006c64491cb8acf2092ce0e0341797fe=1520484212; Hm_lpvt_006c64491cb8acf2092ce0e0341797fe=1520484212; _gscu_1059159971=20484212k04t7612; _gscbrs_1059159971=1; 52710000|PC_clogin=v=1&l=1520482280&e=1520486012330; Hm_lpvt_cb09ebb4692b521604e77f4bf0a61013=1520484215',
            'Host':'ticket.lvmama.com',
            'Origin':'http://ticket.lvmama.com',
            'Referer':'http://ticket.lvmama.com/scenic-10000584',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest',
            'type':'all',
            'currentPage':'11',
            'totalCount':'411'}

#向携程post时的header
def xiecheng_post_header():
    header={'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en,zh-CN;q=0.9,zh;q=0.8',
            'Connection':'keep-alive',
            'Content-Length':'126',
            'Content-Type':'application/x-www-form-urlencoded',
            'Cookie':'_abtest_userid=2d242ab5-7bac-4cc5-97d3-ad6b4ac4b0ce; _RSG=.faQBpeRsOE6mpDfW0xSzB; _RDG=288976db593faf205b2f200cbf30d0f221; _RGUID=e6366e8c-cb6a-4a7e-bf5c-ec0829373c06; UM_distinctid=16130b263e6825-01608b2dd61897-4323461-e1000-16130b263e73bd; __zpspc=9.1.1516940453.1516940453.1%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _ga=GA1.2.1931413397.1516940454; _jzqco=%7C%7C%7C%7C1516940453627%7C1.1769093204.1516940453519.1516940453519.1516940453520.1516940453519.1516940453520.0.0.0.1.1; Union=AllianceID=106201&SID=550003&OUID=v1c5a5ss_DDxeNQUwADhWZAMxUDQINQAm; Session=SmartLinkCode=U550003&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; FD_SearchHistorty={"type":"S","data":"S%24%u5E7F%u5DDE%28CAN%29%24CAN%242018-04-08%24%u5317%u4EAC%28BJS%29%24BJS"}; ASP.NET_SessionSvc=MTAuOC4xODkuNTV8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUxMTk0MzQ3NDkyOA; adscityen=Beijing; bdshare_firstime=1520482162952; _gid=GA1.2.1238423874.1520482165; MKT_Pagesource=PC; appFloatCnt=1; manualclose=1; _bfa=1.1516940450546.3wamio.1.1520482162747.1520522642819.4.7; _bfs=1.1; _RF1=124.205.212.108; Mkt_UnionRecord=%5B%7B%22aid%22%3A%22106201%22%2C%22timestamp%22%3A1520522645684%7D%5D; _bfi=p1%3D290510%26p2%3D290510%26v1%3D7%26v2%3D6',
            'Host':'you.ctrip.com',
            'Origin':'http://you.ctrip.com',
            'Referer':'http://you.ctrip.com/sight/jiashan1019/1473306.html',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'}
    return header

#向携程post时的data
def xiecheng_post_data():
    data={'poiID':'13805941',
            'districtId':'272',
            'districtEName':'Jiashan',
            'pagenow':page,
            'order':'3.0',
            'star':'0.0',
            'tourist':'0.0',
            'resourceId':'1473306',
            'resourcetype':'2'}
    return data





if __name__ == '__main__':
    article_url=""
    page=0

    #大众点评
    # article_url = 'http://www.dianping.com/shop/50527419/review_all/p'
    # for i in range(1,10):
    #     # print (article_url)
    #     page_soup = BeautifulSoup(get_html(article_url), 'html.parser')
    #     get_reviews_from_dianping(page_soup,article_url+str(i),"大众点评")


    #驴妈妈
    # target_url="http://ticket.lvmama.com/vst_front/comment/newPaginationOfComments"
    # for i in range(1,43):
    #     page=i
    #     response=requests.post(target_url,data=lvmama_post_data(),headers=lvmama_post_header())
    #     print(response.status_code)
    #     page_soup = BeautifulSoup(response.text, 'html.parser')
    #     get_reviews_from_lvmama(page_soup,"驴妈妈")

    #携程
    # target_url="http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView"
    # for i in range(1,79):
    #     page=i
    #     response=requests.post(target_url,data=xiecheng_post_data(),headers=xiecheng_post_header())
    #     print(response.status_code)
    #     print(i)
    #     page_soup = BeautifulSoup(response.text, 'html.parser')
    #     get_reviews_from_xiecheng(page_soup,"携程")

