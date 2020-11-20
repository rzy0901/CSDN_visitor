# CSDN_visitor
Use urllib and Beautifulsoup to increase the Page Views to your CSDN Blog.
---
typora-copy-images-to: upload

---

# 爬取某知名网站的数据:smile:

> 爬虫 + 骚操作 = 不讲武德 = 耗子尾汁
>
> 增加你的浏览量

## 需要安装的包

:one:

```
BeautifulSoup
```

:two:

```
urllib
```

>安装方法：
>
>百度 + 随缘 `pip install xxx`

## 代码函数介绍

:one: 

```python
def get_page_url_list(homepage_url, page_number):
    for page in range(1, page_number + 1):
        page_url_list.append("{0}/article/list/{1}".format(homepage_url, page))
    print('page_url_list: ' + page_url_list.__str__())
```

> + 功能：得到你的博客每一页的URL列表
> + homepage_url: 博客主页的URL
> + page_number: 博客的页数
> + <font color="red">注意！这个函数只适用于CSDN，别的博客可以自己观察一下换页之后博客主页的网址形式，再修改代码</font>

:two:

```python
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
```

>+ 功能：得到你的博文的URL列表（全部）
>+ 输入为pageurl_list，即通过`get_page_url_list`得到的列表

:three:

```python
def get_proxy_list():
    for row in urlopen('http://proxylist.fatezero.org/proxy.list').readlines():
        item = json.loads(row)
        if item['type'] == 'http' and item['anonymity'] == 'high_anonymous' and item['response_time'] < 7:
            proxy_list.append(item['host'] + ':' + str(item['port']))
    print("proxy_list" + proxy_list.__str__())
```

>+ 功能：得到代理ip列表（目的为每隔一分钟更换代理ip，防止爬虫被发现）
>
>+ 需要翻墙，所以直接用我跑出来的列表就行了。
>+ 当然也可以选择别的网站获取代理ip的列表。

## 运行案例

![image-20201121010221453](https://sadhorse.oss-cn-beijing.aliyuncs.com/img/image-20201121010221453.png)

+ 我应该已经挂机一段时间了，刷新一下网页界面：(可以看一下我电脑显示的时间)

![image-20201121010427650](https://sadhorse.oss-cn-beijing.aliyuncs.com/img/image-20201121010427650.png)

大约每分钟14个浏览量（你有几篇博文，每分钟有几个浏览量，相当于每分钟拿一个新的ip把你的博文遍历访问一遍）。

## 备注

+ 悠着点用，号没了。

  ![img](https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1605890594&di=46daf93ea23b24c7518bfe4d4fc260bf&src=http://inews.gtimg.com/newsapp_match/0/12783349968/0)

+ ==csdn目前的机制一分钟内无论多少ip访问一篇博文，博文的最大访问量为1==(所以投机取巧是几乎不可能，更换ip意义在于防止爬虫被发现)

+ 更换`User-Agent`以及代理ip防止爬虫被发现

