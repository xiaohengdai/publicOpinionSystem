import os
import re
import time

import uiautomator2 as u2

from config.public_opinion_key_words import COMMON_PUBLIC_OPINION_KEY_WORDS,BUSINESS_LINE_PUBLIC_OPINION_KEY_WORDS

d = u2.connect('38573286')

app_package_name='com.xiaomi.market'

d(textContains='评论').click()
app_name1 = '快手'
app_name2 = '快手极速版'
app_name_list = [app_name1, app_name2]
filter_comment_app_name1=set()
filter_comment_app_name2=set()
filter_comment={app_name_list[0]:filter_comment_app_name1,app_name_list[1]:filter_comment_app_name2}
common_public_opinion_key_words = COMMON_PUBLIC_OPINION_KEY_WORDS
sub_biz='social'

current_dir=os.getcwd()
img_dir=os.path.join(current_dir,'img')
print("img_dir:",img_dir)
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

start_time=time.strftime("%Y_%m_%d_%H_%M_%S")
for i in range (0,22):

    print(f"第{i}次滑动")
    for elem in d(resourceId='com.bbk.appstore:id/comment_content'):
        try:
            comment_text=elem.info.get('text')
        except:
            comment_text =''
        print("comment_text:", comment_text)
        for m in range(0, len(common_public_opinion_key_words)):
            if re.findall(common_public_opinion_key_words[m], comment_text):
                print("用户评论命中通用关键字")
                filter_comment[app_name_list[0]].add(comment_text)
                img_path = os.path.join(img_dir, str(start_time) + '-' + str(i + 1) + '.jpg')
                print("img_path:", img_path)
                d.screenshot(img_path)
        business_line_public_opinion_key_words = BUSINESS_LINE_PUBLIC_OPINION_KEY_WORDS.get(sub_biz)
        for n in range(0, len(business_line_public_opinion_key_words)):
            if re.findall(business_line_public_opinion_key_words[n], comment_text):
                print("用户评论命中业务方关键字")
                filter_comment[app_name_list[0]].add(comment_text)
                img_path = os.path.join(img_dir, str(start_time) + '-' + str(i + 1) + '.jpg')
                print("img_path:", img_path)
                d.screenshot(img_path)
    d.swipe(fx=0.5, fy=0.8, tx=0.5, ty=0.3)
print("filter_comment:",filter_comment)
