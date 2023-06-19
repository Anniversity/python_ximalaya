import requests
from lxml import etree
#from bs4 import BeautifulSoup

# %%
# ————————————————评论数据：墨菲定律————————————————
f = open('mofeidl.txt', 'w+', encoding='utf-8')  # 打开mofeidl文本文件，将墨菲定律爬取的评论存入文本文档中
# 如果想多爬几页可以将20修改为更大的偶数
for i in range(2, 50, 2):
    url = 'https://www.ximalaya.com/album/54445254/?start={}0'.format(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    resp = requests.get(url, headers=headers) # 请求
    resp.encoding = 'UTF-8'
    #print(resp.text)
    e = etree.HTML(resp.text)
    comment1 = e.xpath('// *[ @ id = "anchor_sound_list"] / div[3] / div[3] / div[1] / div / div[3] / p[2] / text()')
    comment2 = e.xpath('//*[@id="anchor_sound_list"]/div[3]/div[3]/div[1]/div/div[3]/div[2]/div/div[2]/p[2]/text()')

    while(i<len(comment1)):
        f.write(str(comment1[i]))
        i += 1
    while(i<len(comment2)):
        f.write(str(comment2[i]))
        i += 1

f.close()
# %%
# ————————————————评论数据：郭德纲21年相声精选————————————————
f = open('guodegang.txt', 'w+', encoding='utf-8') 
for i in range(2, 50, 2):
    url = 'https://www.ximalaya.com/album/9723091/?start={}0'.format(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    resp = requests.get(url, headers=headers)
    resp.encoding = 'UTF-8'
    #print(resp.text)
    e = etree.HTML(resp.text)
    comment1 = e.xpath('//*[@id="anchor_sound_list"]/div[3]/div[3]/div[1]/div/div[3]/p[2]/text()')
    comment2 = e.xpath('//*[@id="anchor_sound_list"]/div[3]/div[3]/div[1]/div/div[3]/div[2]/div/div[2]/p[2]/text()')

    while(i<len(comment1)):
        f.write(str(comment1[i]))
        i += 1
    while(i<len(comment2)):
        f.write(str(comment2[i]))
        i += 1

f.close()
# %%

# %%
# ————————————————评论数据：大奉打更人丨头陀渊丨搞笑&修仙VIP免费有声小说————————————————
f = open('dafengdgr.txt', 'w+', encoding='utf-8') 
for i in range(2, 50, 2):
    url = 'https://www.ximalaya.com/album/47517749/?start={}0'.format(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    resp = requests.get(url, headers=headers)
    resp.encoding = 'UTF-8'
    e = etree.HTML(resp.text)
    comment1 = e.xpath('//*[@id="anchor_sound_list"]/div[3]/div[3]/div[1]/div/div[3]/p[2]/text()')
    #comment2 = e.xpath('//*[@id="anchor_sound_list"]/div[3]/div[3]/div[1]/div[1]/div[3]/div[2]/div/div[2]/p[2]/text()')

    while(i<len(comment1)):
        f.write(str(comment1[i]))
        i += 1
   
f.close()
# %%

# %%
# ————————————————评论数据：10分钟新闻早餐————————————————
f = open('shifenzhxwzc.txt', 'w+', encoding='utf-8') 
for i in range(2, 50, 2):
    url = 'https://www.ximalaya.com/album/68589357/?start={}0'.format(i)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    resp = requests.get(url, headers=headers)
    resp.encoding = 'UTF-8'
    e = etree.HTML(resp.text)
    comment1 = e.xpath('//*[@id="anchor_sound_list"]/div[3]/div[3]/div[1]/div/div[3]/p[2]/text()')

    while(i<len(comment1)):
        f.write(str(comment1[i]))
        i += 1
   
f.close()
# %%