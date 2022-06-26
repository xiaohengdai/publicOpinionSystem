from util.Reptile import Reptile

#参考文章：使用python爬取App安卓应用商店评论并生成词云：https://blog.csdn.net/linchaolong/article/details/122289031

#快手app  id:C33455，快手极速版app id:C100404489
#可以获取快手app的链接:https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum=1&maxResults=25&uri=app%7CC33455&shareTo=&currentUrl=https%253A%252F%252Fappgallery.huawei.com%252Fapp%252FC33455&accessId=&appid=C33455&zone=&locale=zh
#                   https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.user.commenList3&serviceType=20&reqPageNum=%s&maxResults=25&appid=C33455&version=10.0.0&zone=&locale=zh

huawei_channel_app_dict={"快手":"C33455",'快手极速版':'C100404489'}

app_name1='快手'
app_name2='快手极速版'

rep=Reptile()
rep.getHuaWeiAppMarketCommentData(app_name=app_name1,app_id=huawei_channel_app_dict[app_name1])