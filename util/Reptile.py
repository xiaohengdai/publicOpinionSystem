import requests
import json

from data.WriteData import writeCsvFile


class Reptile():
    def getAppstoreUserCommentData(self, pageNum, appId,app_dict):
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
                    rating = dataEntryJson[j]['im:rating']['label']
                    ratinList.append(rating)
                    print("rating:", rating)
                    content = dataEntryJson[j]['content']['label'].replace("\n","")#将评论中内容带的换行默认替换掉，以便存储到.csv文件时数据换行，影响整个文件的结构
                    contentList.append(content)
                    print("content:", content)
                    version = dataEntryJson[j]['im:version']['label']
                    versionList.append(version)
                    print("version:", version)
                    userName = dataEntryJson[j]['author']['name']['label']
                    userNameList.append(userName)
                    print("userName:", userName)
                    writeCsvFile(rating,content,userName,app_dict[appId]+"_rating.csv")
            else:
                print("不存在")
                print("评价总共len(ratinList):"+str(len(ratinList))+"条")
                return i
        print("评价总共len(ratinList):"+str(len(ratinList))+"条")
        return pageNum


    def getQimaiUserCommentData(self, pageNum, appId,channelId,app_dict):
        appIdUrl="https://www.qimai.cn/andapp/comment/appid/"+appId+"/market/"+channelId
        print("appIdUrl:",appIdUrl)
        reponse=requests.request("GET",appIdUrl)
        print("reponse.content:", reponse.content)
        dataDict=json.loads(reponse.content.decode("utf8"))
        print("dataDict:",dataDict)
