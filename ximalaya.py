# 发送请求
# %%
import requests
from lxml import etree
from openpyxl import workbook 
import pandas as pd
import matplotlib 

# import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
resp = requests.get('https://www.ximalaya.com/top/', headers=headers)

# 设置编码
resp.encoding = 'UTF-8'

# 接收服务器给的响应
# print(resp.text)

e = etree.HTML(resp.text)
nums = e.xpath('//*[@id="rankPage"]/div[2]/div/div[2]/div/div/div[2]/div/span/text()') # 排名
names = e.xpath('//*[@id="rankPage"]/div[2]/div/div[2]/div/div/div[2]/div/a/div[2]/div[1]/text()')   # 作品
types = e.xpath('//*[@id="rankPage"]/div[2]/div/div[2]/div/div/div[2]/div/a/div[2]/span[1]/span/text()')    # 类型
authors = e.xpath('//*[@id="rankPage"]/div[2]/div/div[2]/div/div/div[2]/div/a/div[2]/span[@class="user-name mgl-20"]/span/text()')  # 作者
sounds = e.xpath('//*[@id="rankPage"]/div[2]/div/div[2]/div/div/div[2]/div/a/div[2]/span[@class="user-albumcount mgl-20"]/span/text()')  # 声音数
audcount = e.xpath('//*[@id="rankPage"]/div[2]/div/div[2]/div/div/div[2]/div/a/div[2]/span[@class="user-playcount mgl-20"]/span/text()')  # 播放量 单位亿

# 分析
wb = workbook.Workbook()  # 创建Excel对象
ws = wb.active  # 获取当前正在操作的表对象
ws.append(['作品', '作品类型', '作者', '声音数', '播放量'])
datas = []
for name, type, author, sound, aud in zip(names, types, authors, sounds, audcount):
    # re.split(r'[（丨|]', name, maxsplit=-1, flags=0)
    ws.append([name, type, author, sound, aud[:-1]])
    datas.append([name, type, author, sound, aud[:-1]])
    # print(f'{name}--{type}--{author}--{sound}--{aud}')
#wb.save("ximalaya.xlsx")  # 将爬取到的榜单数据绘制excel表格，保存到ximalaya.xlsx中
# %%

df = pd.DataFrame(datas,columns=['作品','作品类型','作者','声音数','播放量'])
# print(df)
# 表格绘制，显示榜单前五十
# df.describe()
df.head(50)

# %%
df_group = df.groupby('作品类型')['作品'].describe().unstack() # 按作品类型作品分组 count-unique-top-freq 取top数据
print("各类型作品top1: ")
print(df_group.top)
# %%

# 设置中文
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold")
# 显示分析图
df.作品类型.hist(edgecolor = 'black')

# %%
df[df.作品类型 == '有声书'].sort_values(by='播放量') #按照某个字段中的数据进行排序
# %%
df['播放量'] = df['播放量'].astype('float') #类型转换
# %%