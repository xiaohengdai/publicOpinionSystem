# **舆情系统搭建**
**系统总共分为以下几个部分**
- 爬App应用市场评分
```
chromedriver下载地址:http://chromedriver.storage.googleapis.com/index.html
遇到问题：
1、当爬取Appstore上某个应用的第11的评论数据时，会抛后面这个错误：CustomerReviews RSS page depth is limited to 10
2、爬取七麦数据上的Android应用评论数据，是加密的，如微信：https://api.qimai.cn/andapp/getCommentList?analysis=eEcbVw9UUUBAH1dVTCdYVQlRWBV8WUNEcBMJDlwPAFMGBVMDAHATAQ%3D%3D
```
- 将相关数据写入csv文件
- 对评分内容进行数据清洗
```
（pandas）评论数据清洗：https://blog.csdn.net/qq_43965708/article/details/110884444
```
- 数据分类，将应用市场评分自动生成三个分类的词库，好评/中性/差评
```
python数据处理——选取csv文件中某几行的数据：https://blog.csdn.net/m0_37876745/article/details/87983308
```
- 单词翻译
```
如果是中文产品的话，将中文翻译成英文
如果是英文产品的话，将英文翻译成中文
```

- 对词库采取合适的分词策略
- 用LSTM训练模型，学习demo:https://github.com/xiaohengdai/SentimentAnalysis
- 从贴吧、微博等其它渠道自动获取到应用数据
- 对其它渠道获取的应用数据进行数据清洗
```
从微博热搜抓取的数据如何做清洗呢？
```
- 用模型来对清洗后的数据进行预测，对其进行分类
- 评价模型，不断迭代
