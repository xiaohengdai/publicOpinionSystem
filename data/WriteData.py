import csv
import os

from common.constant import PROJECTDIR


def writeCsvFile(data1,data2,userName,dstFileName):

    dstFileNamePth=os.path.join(PROJECTDIR,"data",dstFileName)
    print("dstFileNamePth:"+dstFileNamePth)
    f=""
    csvWriter=""
    if not (os.path.exists(dstFileNamePth)):
        os.system("touch "+dstFileNamePth)
        print("创建文件成功")
        print("如若文件不存在，则自动创建并覆盖写入")
        f=open(dstFileNamePth,'w',encoding="utf-8")
        csvWriter = csv.writer(f)
        csvWriter.writerow(["rating", "comment","userName"])
    else:
        print('如若文件已存在，则向文件追加数据')
        f=open(dstFileNamePth,'a',encoding="utf-8")
        csvWriter = csv.writer(f)

    csvWriter.writerow([data1,data2,userName])
    f.close()

# writeCsvFile(1,"test.csv")