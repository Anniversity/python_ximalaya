import jieba
import wordcloud
# %%
# 词云绘制——墨菲定律
f = open('mofeidl.txt', 'r', encoding='utf-8')
content = f.read()
f.close()
word = jieba.lcut(content)  # 将中文的文本通过分词获得单个词语
txt = ' '.join(word)  # 空格拼接
w = wordcloud.WordCloud(font_path='c:\windows\Fonts\STZHONGS.TTF', width=1000, height=700, background_color='white')
w.generate(txt)  # generate函数:用于生成词云图的函数
w.to_file('mofeidl.png')
# %%

# %%
# 词云绘制——郭德纲21年相声精选
f = open('guodegang.txt', 'r', encoding='utf-8')
content = f.read()
f.close()
word = jieba.lcut(content)  # 将中文的文本通过分词获得单个词语
txt = ' '.join(word)  # 空格拼接
w = wordcloud.WordCloud(font_path='c:\windows\Fonts\STZHONGS.TTF', width=1000, height=700, background_color='white')
w.generate(txt)  # generate函数:用于生成词云图的函数
w.to_file('guodegang.png')
# %%

# %%
# 词云绘制——大奉打更人
f = open('dafengdgr.txt', 'r', encoding='utf-8')
content = f.read()
f.close()
word = jieba.lcut(content)  # 将中文的文本通过分词获得单个词语
txt = ' '.join(word)  # 空格拼接
w = wordcloud.WordCloud(font_path='c:\windows\Fonts\STZHONGS.TTF', width=1000, height=700, background_color='white')
w.generate(txt)  # generate函数:用于生成词云图的函数
w.to_file('dafengdgr.png')
# %%

# %%
# 词云绘制——10分钟新闻早餐
f = open('shifenzhxwzc.txt', 'r', encoding='utf-8')
content = f.read()
f.close()
word = jieba.lcut(content)  # 将中文的文本通过分词获得单个词语
txt = ' '.join(word)  # 空格拼接
w = wordcloud.WordCloud(font_path='c:\windows\Fonts\STZHONGS.TTF', width=1000, height=700, background_color='white')
w.generate(txt)  # generate函数:用于生成词云图的函数
w.to_file('shifenzhxwzc.png')
# %%