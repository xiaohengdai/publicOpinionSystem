from util.reptile import Reptile

rep=Reptile()
kmallAppId="1188224117"
ratingPageNum=rep.getAppstoreUserCommentData(3,kmallAppId)#快驴id
print("ratingPageNum:",ratingPageNum)