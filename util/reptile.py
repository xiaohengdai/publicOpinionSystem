import requests
import json


class Reptile():
    def getAppstoreUserCommentData(self, pageNum, appId):
        ratinList=[]
        contentList=[]
        versionList=[]
        userNameList=[]
        for i in range (0,pageNum):
            # pageNum=1
            appIdUrl = "https://itunes.apple.com/CN/rss/customerreviews/page=" + str(i+1) + "/id=" + str(
                appId) + "/sortby=mostrecent/json?l=en&cc=cn"
            print("获取第" + str(i+1) + "页数据")
            print("appIdUrl:" + appIdUrl)
            response = requests.request("GET", appIdUrl)
            # data=response.text
            dataDict = json.loads(response.content.decode('utf8'))
            # print("data_json:" + data_json)
            dataUpdated = dataDict['feed']['updated']
            print("评论更新时间: " + str(dataUpdated))
            if ("entry" in dataDict['feed'].keys()):
                print("存在")
                dataEntryJson = dataDict['feed']['entry']
                dataEntryJsonLen = len(dataEntryJson)
                print("评论data_entry_json_len共有:" + str(dataEntryJsonLen) + "个")
                for j in range(0, dataEntryJsonLen):
                    rating = dataEntryJson[j]['im:rating']
                    ratinList.append(rating)
                    print("rating:", rating)
                    content = dataEntryJson[j]['content']
                    contentList.append(content)
                    print("content:", content)
                    version = dataEntryJson[j]['im:version']
                    versionList.append(version)
                    print("version:", version)
                    userName = dataEntryJson[j]['author']['name']
                    userNameList.append(userName)
                    print("userName:", userName)
            else:
                print("不存在")
                print("评价总共len(ratinList):"+str(len(ratinList))+"条")
                return i
        print("评价总共len(ratinList):"+str(len(ratinList))+"条")
        return pageNum

