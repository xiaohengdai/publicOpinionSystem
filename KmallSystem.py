from util.Reptile import Reptile
#快驴华为渠道评论，https://www.qimai.cn/andapp/comment/appid/2307715/market/6


#微信华为渠道评论，https://www.qimai.cn/andapp/comment/appid/9/market/6

app_dict={"1188224117":"iOS_快驴","414478124":"iOS_微信","2307715":"Android_快驴","9":"Android_微信"}
channel_dict={"6":"HuaWei"}

rep=Reptile()
kmallAppId="414478124"
ratingPageNum=rep.getAppstoreUserCommentData(10,kmallAppId,app_dict)#快驴id
print("ratingPageNum:",ratingPageNum)

# kmallAndroidId="2307715"
# wechatAndroidId="9"
# huaWeiChannelId="6"
# rep.getQimaiUserCommentData(10,wechatAndroidId,huaWeiChannelId,app_dict)