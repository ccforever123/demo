import requests
import re
import jieba
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.rcParams['figure.figsize'] = (15.0, 10.0)
from wordcloud import WordCloud

def get_text(url):
	r = requests.get(url)
	r.encoding = r.apparent_encoding
	if r.status_code == 200:
		return r.text
	else:
		return 0

def get_shop_info(page):
	url = 'http://restapi.amap.com/v3/place/text?key=910cc97a063204c50d509ecb492afbe1&keywords=奶茶&types=冷饮店&city=厦门&children=1&offset=50&page=%s&extensions=all' % page
	text = get_text(url)
	reg_name = re.compile(r'\"name\":\"(.*?)\"')
	name_list = reg_name.findall(text)
	return name_list

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

		if word in ['奶','茶','咖','啡','店']:
			continue
		elif word in dict:
			dict[word] = dict[word]+1
		else:
#			print(word)
			dict[word] = 1
	wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', max_font_size=80).fit_words(dict)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis('off')
	plt.show()


def save_to_txt(name_list):
	for i in range(len(name_list)):
#		print("%s" % (name_list[i]))
		with open('name.txt', 'a', encoding='utf-8') as f:
			f.write("%s\n" % (name_list[i]))

def main():
	page = 1
	while True:
		print('Page = %s' % page)
		name_list = get_shop_info(page)
		if name_list == 0:
			print('DONE')
			quit()
		else:
			save_to_txt(name_list)
			page+=1

def main1():
	with open('name.txt', 'r', encoding='utf-8') as f:
		name_list = f.readlines()
		name_check = []
		for i in range(len(name_list)):
			name = name_list[i].split('(')[0]
			name = name.split('\n')[0]
			if name in name_check:
				continue
			else:
				name_check.append(name)
#			print(name)
			with open('new_name.txt', 'a', encoding='utf-8') as f:
				f.write("%s" % (name))

def main2():
	with open('new_name.txt', 'r', encoding='utf-8') as f:
		name_list = f.read()
#		print(name_list)
		word_sep(name_list)

if __name__ == '__main__':
    main2()