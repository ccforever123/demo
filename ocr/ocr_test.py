#!usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import os
import shutil

def get_bin_table(threshold = 140):
	# 获取灰度转二值的映射table
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table

def get_text(parent, filename):
	img_path = os.path.join(parent, filename)
	image = Image.open(img_path)
	imgry = image.convert('L')  # 转化为灰度图
	table = get_bin_table()
	out = imgry.point(table, '1')
	out.save(parent + '\\out\\%s' % filename, 'bmp')
#	Image._show(out)
	try:
		text = pytesseract.image_to_string(out, config='digits')
		# 去除数字以外的其他字符
		fil = filter(str.isdigit, text)
		new_text = ''
		for i in fil:
			new_text += i
		print('%s.bmp 已被识别为: %s' %(filename, new_text))
		if os.path.isfile(parent + '\\out\\%s.bmp' % new_text):
			print('%s.bmp 已存在，删除。' % new_text)
			os.remove(parent + '\\out\\%s.bmp' % new_text)
			os.remove(parent + '\\out\\%s.jpg' % new_text)
		os.rename(parent + '\\out\\%s' % filename, parent + '\\out\\%s.bmp' % new_text)
		shutil.copyfile(os.path.join(parent, filename), parent + '\\out\\%s.jpg' % new_text)

	except Exception as e:
		print(e)

def main():
	# 家里路径
	# path = 'E:\\Documents\\PycharmProjects\\PythonLearning\\Python-study\\demo\\ocr\\img'
	# 公司路径
	path = 'E:\\Documents\\PycharmProjects\\demo\\ocr\\img'
	for parent, dirnames, filenames in os.walk(path):
		for filename in filenames:
			text = get_text(parent, filename)

if __name__ == '__main__':
    main()
