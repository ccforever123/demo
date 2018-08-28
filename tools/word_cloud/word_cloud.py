import re
import jieba
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

def get_cleaned_comment(comments):
	#数据清洗
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
	#词频统计.设置字体，大小和颜色
	words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": np.size})
	words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
	# 用词云进行显示，生成词频字典
	word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

	image = Image.open('psp.jpg')
	graph = np.array(image)
	wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', max_font_size=120, mask=graph).fit_words(word_frequence)
	image_color = ImageColorGenerator(graph)
	plt.figure()
	plt.imshow(wordcloud)
	plt.imshow(wordcloud.recolor(color_func=image_color))
	plt.axis('off')
	plt.savefig('output.jpg', dpi=300)
	plt.show()

with open('词云.txt', 'r', encoding= 'gbk') as f:
	text = f.read()
	comment = get_cleaned_comment(text)
	word_cloud(text)
