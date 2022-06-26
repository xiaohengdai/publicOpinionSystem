# 2.2 面向对象实现实现翻页
import requests
import csv
import time

class XiaomoShop():
    def __init__(self):
        self.url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId=6&pageSize=30'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47'
        }
    def get_url(self, url):
        print("url:",url)
        res = requests.get(url, headers=self.headers)
        result = res.json()['data']
        return result
    def parse_url(self, html):
        app_data = []
        for app in html:
            item = {}
            item['name'] = app['displayName']
            item['itemize'] = app['level1CategoryName']
            item['url'] = 'https://app.mi.com/details?id=' + app['packageName']
            app_data.append(item)
        return app_data
    def save_data(self, lis_data):
        header = ['name', 'itemize', 'url']
        with open('xiaomi_data2.csv', 'a', encoding='utf-8', newline="") as f:
            writ = csv.DictWriter(f, header)
            if i == 0:
                writ.writeheader()
            writ.writerows(lis_data)
    def main(self):
        global i
        for i in range(3):
            new_url = self.url.format(i)
            html = self.get_url(new_url)
            lis_data = self.parse_url(html)
            self.save_data(lis_data)
            # time.sleep(2)

if __name__ == '__main__':
    start_time = time.time()
    X = XiaomoShop()
    X.main()
    end_time = time.time()
    print('程序运行时间：%s' % (end_time - start_time))
