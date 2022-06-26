#!/usr/bin/python
# coding=utf8
# -*- encoding: UTF-8 -*-
# import requests,json
import requests
import json
# 导入import模块
import sys




class AFNet(object):

    # 接口中获取feed
    def arrFromDic(self, dic):
        user_dic = json.loads(dic)
        feed = user_dic['feed']
        entry = feed['entry']
        return entry
        pass

    # 获取详细信息
    def getInfo(self, page, ids):
        url = "https://itunes.apple.com/cn/rss/customerreviews/page=%s/id=%s/sortby=mostrecent/json" % (page, ids)

        afn = AFNet()
        response = afn.get(url)
        return response
        pass

    # get请求
    def get(self, url):
        print("url:",url)
        response = requests.get(url=url)
        return response
        pass

    # post请求
    def post(self, url, parmars):
        print(url)
        print(parmars)
        requests.post(url=url, data={'key1': 'value1', 'key2': 'value2'},
                      headers={'Content-Type': 'application/x-www-form-urlencoded'})
        response = requests.get(url=url)
        return response.text
        pass


# 请求类的初始化
afn = AFNet()
# app的id
ids = '930368978'
# 全局变量 最终所有接口数据源
entry = []
# 便历接口
for page in range(1, 100000000):

    st = afn.getInfo(page, ids)
    text = st.text
    count = len(text)
    print (count)

    if count > 47:
        # 接口数据解析获取评论数据
        entry2 = afn.arrFromDic(text)
        entry = entry + entry2
        count = len(entry2)
        text = "页数=%s  数量=%s" % (page, count)
        print(text)
        pass

    if count <= 47:
        # print text
        break
        pass

    pass
arrResult = []
for dic in entry:

    # print dic
    # print "\n"

    author = dic["author"]

    name = author["name"]
    namelabel = name["label"]

    content = dic["content"]
    contentlabel = content["label"]

    title = dic["title"]
    titlelabel = title["label"]

    version = dic["im:version"]
    versionlabel = version["label"]

    rating = dic["im:rating"]
    ratinglabel = rating["label"]

    voteSum = dic["im:voteSum"]
    voteSumlabel = voteSum["label"]

    resultSrr = ""
    start = ""
    for x in range(0, int(ratinglabel)):
        start = start + "⭐️"
        pass

    resultSrr = resultSrr + "…………………………………………………………………………………………\n"
    resultSrr = resultSrr + "版本= %s\n" % (versionlabel)
    resultSrr = resultSrr + "星数= %s\n" % (start)
    resultSrr = resultSrr + "评级= %s\n" % (ratinglabel)
    resultSrr = resultSrr + "昵称= %s\n" % (namelabel)
    resultSrr = resultSrr + "标题= %s\n" % (titlelabel)
    resultSrr = resultSrr + "内容= %s\n" % (contentlabel)
    resultSrr = resultSrr + "投票= %s\n" % (voteSumlabel)

    print (resultSrr)

    arrResult.append(resultSrr)
    pass
# print arrResult
count = len(entry)
text = "总数=%s" % (count)
# print text
f = open('feedList.txt', mode='w')
# 数据保存
str1 = json.dumps(entry)  # 字典转字符串
str1 = ''.join(arrResult)  # 数组转字符串
f.write(str1)  # write 写入
f.close()  # 关闭文件