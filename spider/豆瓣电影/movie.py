from urllib import request
import re
import jieba
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud

#https://segmentfault.com/a/1190000010473819

def get_html_data(url):
	r = request.urlopen(url)
	html_data = r.read().decode('utf-8')
	'''
	保存html数据到txt
	with open('html.txt', 'w', encoding='utf-8') as f:
		f.write(html_data)
	'''
	return html_data

def get_vote_data(comments,html_data):
	reg_vote = r'allstar(.)0 rating\"'
	reg_comment = r'<p class=""> (.*?)</p>'
	list_vote = re.compile(reg_vote).findall(html_data)
	list_comment = re.compile(reg_comment, re.S).findall(html_data)

	#爬取评论信息comments
	for i in range(len(list_comment)):
		comments = comments + list_comment[i]
	return comments

def get_cleaned_comment(comments):
	#评论数据清洗
	pattern = re.compile(r'[\u4e00-\u9fa5]+', re.S)
	filter_comment = pattern.findall(comments)
	cleaned_comment = ''.join(filter_comment)
	return cleaned_comment

def word_cloud(cleaned_comment):
	# 分词
	segment = jieba.lcut(cleaned_comment)
	words_df = pd.DataFrame({'segment': segment})

	# 去除无意义的停用词
	stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='utf-8')  # quoting=3全不引用
	words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
	#print(words_df)

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

def main():
	comments = ''
	page = 10
	for i in range(page):
		n = i * 20
		url = 'https://movie.douban.com/subject/26363254/comments?start=%s&limit=20&sort=new_score&status=P' % n
		html_data = get_html_data(url)
		comments = get_vote_data(comments, html_data)
		print(i / page * 100, ' %')

	cleaned_comment = get_cleaned_comment(comments)
	word_cloud(cleaned_comment)


if __name__ == '__main__':
	main()