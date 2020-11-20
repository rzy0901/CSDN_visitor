import random
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import datetime
from threading import Thread
import time

page_url_list = []

article_list = []

# 这个不要改，预设好的代理ip
proxy_list = ['3.211.17.212:80', '208.80.28.208:8080', '169.57.1.84:8123',
              '208.81.193.205:80', '51.81.113.246:80', '138.197.157.16:80',
              '52.170.221.245:80', '134.209.162.216:80', '204.13.164.179:80', '159.8.114.37:80', '159.8.114.37:8123',
              '62.102.235.187:80', '195.201.74.70:80', '83.96.237.121:80', '169.57.157.148:80', '78.47.16.54:80',
              '159.8.114.34:8123', '161.202.226.194:8123', '23.91.96.251:80', '80.48.119.28:8080', '119.81.189.194:80',
              '103.115.14.43:80', '149.28.28.66:80', '119.81.71.27:8123', '119.81.71.27:80', '181.94.244.49:8080',
              '119.206.242.196:80', '136.243.254.196:80', '122.147.141.151:80', '45.202.9.160:8888',
              '51.75.147.43:3128', '68.94.189.60:80', '60.255.151.82:80', '58.218.239.164:4216', '162.144.50.197:3838',
              '149.28.157.229:3128', '180.250.12.10:80', '150.109.32.166:80', '115.223.7.110:80', '47.98.112.7:80',
              '43.254.221.27:80', '101.132.143.232:80', '223.82.106.253:3128', '46.4.129.54:80', '14.63.228.217:80',
              '82.200.233.4:3128', '165.22.66.91:80', '80.253.247.42:3838', '116.254.116.99:8080', '51.75.147.44:3128',
              '132.145.18.53:80', '135.181.68.88:3128', '162.144.46.168:3838', '51.15.157.182:3838',
              '212.83.161.110:3838', '162.144.48.139:3838', '47.75.90.57:80', '162.144.48.236:3838', '51.81.82.175:80',
              '31.14.49.1:8080', '195.154.242.205:3838', '163.172.127.248:3838', '51.75.147.35:3128',
              '182.52.238.119:40456', '212.129.32.41:3838', '110.44.117.26:43922', '40.121.91.147:80',
              '13.233.254.153:80', '193.110.115.220:3128', '79.134.7.134:48900', '128.199.83.56:9999']

User_Agent = [
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; OMNIA7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 60; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)"
]


def get_page_url_list(homepage_url, page_number):
    for page in range(1, page_number + 1):
        page_url_list.append("{0}/article/list/{1}".format(homepage_url, page))
    print('page_url_list: ' + page_url_list.__str__())


def get_article_list(pageurl_list):
    for page_url in pageurl_list:
        response = requests.get(page_url, headers={'User-Agent': User_Agent[random.randint(0, len(User_Agent) - 1)],
                                                   'referer': 'http://blog.csdn.net'})
        soup = BeautifulSoup(response.content, 'lxml')
        h4 = soup.find_all("h4")
        for h in h4:
            if h is not None:
                article_list.append(h.a["href"])
            else:
                pass
    print("article_list" + article_list.__str__())


def get_proxy_list():
    for row in urlopen('http://proxylist.fatezero.org/proxy.list').readlines():
        item = json.loads(row)
        if item['type'] == 'http' and item['anonymity'] == 'high_anonymous' and item['response_time'] < 7:
            proxy_list.append(item['host'] + ':' + str(item['port']))
    print("proxy_list" + proxy_list.__str__())


def run():
    while True:
        for proxy in proxy_list:
            proxy = {'http': proxy}
            for article in article_list:
                header = {'User-Agent': User_Agent[random.randint(0, len(User_Agent) - 1)]}
                try:
                    requests.get(article, headers=header, proxies=proxy, timeout=7)
                    print('ok ip:' + proxy['http'] + 'article:' + article)
                except:
                    print('no')
                    if proxy['http'] in proxy_list:
                        proxy_list.remove(proxy['http'])
            time.sleep(60)  # 哎呀，我服了，csdn好像在一分钟以内即使由多个不同的代理ip来访问它，它的访问量还是为1.（也就是一分钟内，你每一篇文章的最大访问量永远为1）
            # 妈的，草鸡玩意，太精明了


if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    # get_proxy_list()  # 这玩意需要翻墙才可以爬取，而且有时候不成，所以直接用现成的就行。
    get_page_url_list(homepage_url='https://blog.csdn.net/qq_45504981', page_number=1)
    get_article_list(pageurl_list=page_url_list)
    mission = list()  # 多线程跑的快
    nums = 50
    for i in range(nums):
        mission.append(Thread(target=run()))
    for i in range(nums):
        # mission[i].setDaemon(True)
        mission[i].start()
    for i in range(nums):
        mission[i].join()
