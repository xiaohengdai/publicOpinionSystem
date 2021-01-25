# **舆情系统搭建**
**系统总共分为以下几个部分**
- 爬App应用市场评分
- 将相关数据存库
- 将应用市场评分自动生成三个分类的词库，好评/中性/差评
- 对词库采取合适的分词策略
- 用LSTM训练模型，学习demo:https://github.com/xiaohengdai/SentimentAnalysis
- 用模型来预测从贴吧等其它渠道获取到的应用数据，对其进行分类
