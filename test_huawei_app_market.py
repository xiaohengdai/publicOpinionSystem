# -*- coding: utf-8 -*-
import re
from typing import List

import requests
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import pandas as pd
from time import sleep

from config.public_opinion_key_words import COMMON_PUBLIC_OPINION_KEY_WORDS, BUSINESS_LINE_PUBLIC_OPINION_KEY_WORDS


@dataclass_json
@dataclass
class Comment:
    accountId: str
    accountName: str
    approveCounts: str
    cipherVersion: str
    commentAppId: str
    commentId: str
    commentInfo: str
    commentType: str
    id: str
    isAmazing: int
    isModified: int
    levelUrl: str
    logonId: str
    nickName: str
    phone: str
    operTime: str
    photoUrl: str
    rating: str
    replyComment: str
    replyCounts: int
    serviceType: str
    stars: str
    title: str
    versionName: str


@dataclass_json
@dataclass
class CommentPage:
    # totalPages: int
    count: int
    devWords: List[str]
    list: List[Comment]
    encoding: str = 'utf-8'


class HuaweiSpider:

    @staticmethod
    def commentPage(page,app_id) -> CommentPage:
        """
        评论分页
        :param page: 页码，从1开始
        :return:
        """
        url = f"https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=%s&maxResults=25&appid={app_id}&version=10.0.0&zone=&locale=zh" % page
        print("url:",url)
        r = requests.get(url, headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,ko;q=0.8,und;q=0.7,en;q=0.6,zh-TW;q=0.5,ja;q=0.4',
            'Connection': 'keep-alive',
            'Host': 'web-drcn.hispace.dbankcloud.cn',
            'Referer': 'https://appgallery.huawei.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        }, verify=False)
        r.encoding = r.apparent_encoding
        if r and r.status_code == 200:
            # print(r.content)
            content = CommentPage.from_json(r.content)
            content.encoding = r.encoding
            return content


if __name__ == '__main__':



    huawei_channel_app_dict = {"快手": "C33455", '快手极速版': 'C100404489'}

    app_name1 = '快手'
    app_name2 = '快手极速版'
    app_name_list=[app_name1,app_name2]
    sub_biz='social'
    filter_comment={}
    for j in range (0,len(app_name_list)):
        filter_comment[app_name_list[j]]=[]
        data = []
        page = 1
        columns = ['用户名', '评论', '评分', '评论时间', '版本号', '设备']
        while True:
            commentPage = HuaweiSpider().commentPage(page,app_id=huawei_channel_app_dict[app_name_list[j]])

            if len(commentPage.list) > 0:
                # print(commentPage)
                for row in commentPage.list:
                    print("row.commentInfo:",row.commentInfo)
                    common_public_opinion_key_words = COMMON_PUBLIC_OPINION_KEY_WORDS
                    for m in range (0,len(common_public_opinion_key_words)):
                        if re.findall(common_public_opinion_key_words[m],row.commentInfo):
                            print("用户评论命中通用关键字")
                            filter_comment[app_name_list[j]].append([row.nickName, row.commentInfo, row.stars, row.operTime, row.versionName, row.phone])
                    business_line_public_opinion_key_words = BUSINESS_LINE_PUBLIC_OPINION_KEY_WORDS.get(sub_biz)
                    for n in range(0,len(business_line_public_opinion_key_words)):
                        if re.findall(business_line_public_opinion_key_words[n], row.commentInfo):
                            print("用户评论命中业务方关键字")
                            filter_comment[app_name_list[j]].append(
                                [row.nickName, row.commentInfo, row.stars, row.operTime, row.versionName, row.phone])
                    data.append([row.nickName, row.commentInfo, row.stars, row.operTime, row.versionName, row.phone])
                page += 1
                sleep(2)
            else:
                break

        df = pd.DataFrame(data, columns=columns)
        df.to_excel(f'华为应用商店{app_name_list[j]}App评论.xlsx', index=False)
    print("filter_comment:",filter_comment)
