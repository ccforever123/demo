import requests
import re
import jieba
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)
from wordcloud import WordCloud


def get_text(url):
	r = requests.get(url)
	r.encoding = r.apparent_encoding
	return r.text

def word_cloud(name_list):
	# 分词
	segment = jieba.lcut(name_list)
	words_df = pd.DataFrame({'segment': segment})

	# 去除无意义的停用词
	stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
	                        encoding='utf-8')  # quoting=3全不引用
	words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
	#词频统计.设置字体，大小和颜色
	#wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', max_font_size=80)
	words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
	words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
	#print(words_stat.head)

	# 用词云进行显示，生成词频字典
	word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
	#print(word_frequence)

	'''word_frequence_list = []
	for key in word_frequence:
		temp = (key, word_frequence[key])
		word_frequence_list.append(temp)
	#print(word_frequence_list)'''

	wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', max_font_size=80).fit_words(word_frequence)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()

def word_sep(text):
	dict = {}
	for word in text:
		if word in ['便','利','店','超','市','（','）','(',')','食','杂','百','货','小','卖','部','2','4','批','发','见','福']:
			continue
		elif word in dict:
			dict[word] = dict[word]+1
		else:
			dict[word] = 1
	wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', max_font_size=80).fit_words(dict)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()

name_all = ''
'''
for page in range(1,101):
	print('Page: %s / 100' % page)
	url = 'http://restapi.amap.com/v3/place/text?&keyword=&types=060200&city=350200&citylimit=true&&output=xml&offset=25&page=%s&key=910cc97a063204c50d509ecb492afbe1&extensions=base' % page
	text = get_text(url)
	reg_name = re.compile(r'<name>(.*?)</name>')
	name_list = reg_name.findall(text)
	for name in name_list:
		name_all = name_all+name
	with open('name.txt', 'w') as f:
		f.write(name_all)
'''
with open('name.txt', 'r') as f:
	text = f.read()
#	word_cloud(text)
	word_sep(text)