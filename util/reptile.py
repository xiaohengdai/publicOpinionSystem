import requests
import json

class  Reptile():
    def getAppstoreUserCommentData(self,appId):
        page_num=1
        appIdUrl="https://itunes.apple.com/CN/rss/customerreviews/page="+page_num+"/id="+appId+"/sortby=mostrecent/json?l=en&cc=cn"
        print("获取第"+page_num+"页数据")
        print("appIdUrl:"+appIdUrl)
        response=requests.request("GET",appIdUrl)
        # data=response.text
        data_dict=json.loads(response.content.decode('utf8'))
        # print("data_json:" + data_json)
        data_updated=data_dict['feed']['updated']
        print("评论更新时间: "+data_updated)
        data_entry_json=data_dict['feed']['entry']
        data_entry_json_len=len(data_entry_json)
        print("评论data_entry_json_len共有:"+str(data_entry_json_len)+"个")
        for i in range (0,data_entry_json_len):
            rating=data_entry_json[i]['im:rating']
            print("rating:",rating)
            content=data_entry_json[i]['content']
            print("content:",content)
            version=data_entry_json[i]['im:version']
            print("version:",version)
            user_name=data_entry_json[i]['author']['name']
            print("user_name:",user_name)


