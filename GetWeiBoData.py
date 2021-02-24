import os
import requests
import bs4
from common.constant import PROJECTDIR

mylist=[]
weibot_hotsearch_url='https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
r = requests.get(url=weibot_hotsearch_url,timeout=10)
# print("r.status_code:",r.status_code)  # 获取返回状态
r.encoding=r.apparent_encoding
# print("r.encoding:",r.encoding)
demo = r.text
# print("demo:",demo)
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
for link in soup.find('tbody') :
    hotnumber=''
    if isinstance(link,bs4.element.Tag):
#        print(link('td'))
        lis=link('td')
        # print("lis[1]:",lis[1])
        # print("lis[1]('a'):",lis[1]('a'))
        hotrank=lis[0].string
        hotkeyword=lis[2].string  #热搜是新、热还是沸腾
        hotname=lis[1]('a')[0].string#热搜名称
        # print("hotname:",hotname)
        hotnumber_span=lis[1].find('span')
        # print("hotnumber_span:", hotnumber_span)
        if isinstance(hotnumber_span,bs4.element.Tag):
            hotnumber=hotnumber_span.string#热搜指数
            # print("hotnumber:",hotnumber)
            pass
        mylist.append([hotrank,hotname,hotnumber,hotkeyword])
dstFileNamePth=os.path.join(PROJECTDIR,"data","weibo.csv")
f=open(dstFileNamePth,"w+")
for line in mylist:
    f.write('%s %s %s %s\n'%(line[0],line[1],line[2],line[3]))