import pandas
import os
import numpy as np

from common.constant import PROJECTDIR


def cleanData(csv_file_name):
    df=pandas.read_csv(os.path.join(PROJECTDIR,"data",csv_file_name),encoding="utf-8")
    # print("df:",df)
    #1、空值处理
    df=df.dropna(subset=['comment'])#空值处理:直接删除评论列中的空值（不包含空字符串）
    # print(df.dropna(subset=['comment']))
    #2、数据去重
    df.drop_duplicates(subset=[ 'comment','userName'], keep='first', inplace=True)# 根据用户id与comment两列作为参照，如存在用户id与comment同时相同，那么只保留最开始出现的。
    # print("df:",df)
    df.reset_index(drop=True, inplace=True) # 重置索引
    # print("df:", df)
    #3、定向剔除无用评论
    df['comment'] = df['comment'].str.replace('^[0-9]*$', '')  #剔除纯数字评论，先将其转为空字符串，用空字符串('')替换纯数字('123')

    # 将空字符串转为'np.nan',即NAN,用于下一步删除这些评论
    df['comment'].replace(to_replace=r'^\s*$', value=np.nan, regex=True, inplace=True)
    # 删除comment中的空值，并重置索引
    df = df.dropna(subset=['comment'])
    df.reset_index(drop=True, inplace=True)
    # print("df:",df)
    df.to_csv(os.path.join(PROJECTDIR, "data", "clear_data_" + csv_file_name), index=False, encoding='utf-8')
cleanData("iOS_微信_rating.csv")