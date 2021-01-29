import csv
import os

def writeCsvFile(data1,data2,dstFileName):
    currentDir=os.path.abspath(os.path.dirname(__file__))
    print("currentDir:",currentDir)
    dstFileNamePth=os.path.join(currentDir,dstFileName)
    print("dstFileNamePth:"+dstFileNamePth)
    f=""
    if not (os.path.exists(dstFileNamePth)):
        os.system("touch "+dstFileNamePth)
        print("创建文件成功")
        print("如若文件不存在，则自动创建并覆盖写入")
        f=open(dstFileNamePth,'w',encoding="utf-8")
    else:
        print('如若文件已存在，则向文件追加数据')
        f=open(dstFileNamePth,'a',encoding="utf-8")
    print("执行第几次")
    csvWriter=csv.writer(f)
    csvWriter.writerow([data1,data2])
    f.close()

# writeCsvFile(1,"test.csv")