# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
import os, sys
import cv2
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def main():
	path = sys.path[0]
	img_path = os.path.join(path,'img')
	save_path = os.path.join(path,'save')
	output_path = os.path.join(path, 'out')
	for parents, dirnames, filenames in os.walk(img_path):
		for filename in filenames:
			img = cv2.imread(os.path.join(img_path, filename), 0)
			blur_img = cv2.blur(img, (3,3))
			plt.subplot(121), plt.imshow(img), plt.title('Original')
			plt.subplot(122), plt.imshow(blur_img), plt.title('Averaging')
#			plt.show()

#			cv2.imshow('Salt', result)
#			cv2.imshow('Median', blur)

#			blur_img.save(os.path.join(save_path, '%s.bmp') % filename[:-4])
			print('已生成%s灰度图' % filename)
			get_text(blur_img, filename, output_path)

#			cv2.waitKey(0)
def get_bin_table(threshold = 210):
	# 获取灰度转二值的映射table
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table

def get_text(out, filename, output_path):
	print('-> 正在对 %s 进行文字识别' % (filename))
#	img_path = os.path.join(parent, filename)
#	image = Image.open(img_path)
#	imgry = image.convert('L')  # 转化为灰度图
#	table = get_bin_table()
#	out = imgry.point(table, '1')
#	out_path = os.path.join(parent, 'out')
#	if os.path.isdir(out_path) == False:
#		os.mkdir(out_path)
#	out.save(os.path.join(out_path, '%s.bmp') % filename[:-4])
#	print('已生成%s灰度图' % filename)
#	Image._show(out)
	try:
		text = pytesseract.image_to_string(out, lang='chi_sim')
		text = remove_space(text)

		if os.path.isdir(output_path) == False:
			os.mkdir(output_path)
		with open(output_path + '%s.txt' % filename[:-4], 'w') as f:
			f.write(text)
			print(' √ %s 文字识别已完成，保存在：%s' % (filename, os.path.join(output_path, '%s.txt') % filename[:-4]))
#		print(text)
	except Exception as e:
		print(e)

def remove_space(text):
	new_text = ''
	j = ''
	for i in text:
		if (j != ' ' and i == ' ') or (j != '\n' and i == '\n'):
			j = i
			continue
		else:
			j = i
			new_text += i
	return new_text

if __name__ == '__main__':
	main()