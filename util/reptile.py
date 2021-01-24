import requests
import json

class  Reptile():
    def getAppstoreUserCommentData(self,appId):
        appIdUrl="https://itunes.apple.com/CN/rss/customerreviews/page=1/id="+appId+"/sortby=mostrecent/json?l=en&cc=cn"
        print("appIdUrl:"+appIdUrl)
        response=requests.get(appIdUrl)
        data=response.text
        data_json=json.dumps(data)
        print("data_json:" + data_json)
        data_updated_json=data_json['feed']['updated']
        data_entry_json=data_json['feed']['entry']
        data_entry_json_len=len(data_entry_json)
        print("评论data_entry_json_len共有:"+data_entry_json_len+"个")
        for i in range (0,data_entry_json_len):
            rating=data_entry_json[i]['im:rating']
            print("rating:",rating)
            content=data_entry_json['content']
            print("content")
            version=data_entry_json['im:version']
            user_name=data_entry_json['author']['name']


