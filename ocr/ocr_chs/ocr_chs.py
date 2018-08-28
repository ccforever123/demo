# -*-encoding:utf-8-*-
# Author: cc
# Version: V1.02
from PIL import Image
import pytesseract
import os, sys

def get_bin_table(threshold = 210):
	# 获取灰度转二值的映射table
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table

def get_text(parent, filename):
	print('-> 正在对 %s 进行文字识别' % (filename))
	img_path = os.path.join(parent, filename)
	image = Image.open(img_path)
	imgry = image.convert('L')  # 转化为灰度图
	table = get_bin_table()
	out = imgry.point(table, '1')
#	out_path = os.path.join(parent, 'out')
#	if os.path.isdir(out_path) == False:
#		os.mkdir(out_path)
#	out.save(os.path.join(out_path, '%s.bmp') % filename[:-4])
#	print('已生成%s灰度图' % filename)
#	Image._show(out)
	try:
		text = pytesseract.image_to_string(out, lang='chi_sim')
		text = remove_space(text)
		txt_path = os.path.join(parent, 'txt')
		if os.path.isdir(txt_path) == False:
			os.mkdir(txt_path)
		with open(parent + '\\txt\\%s.txt' % filename[:-4], 'w') as f:
			f.write(text)
			print(' √ %s 文字识别已完成，保存在：%s' % (filename, os.path.join(txt_path, '%s.txt') % filename[:-4]))
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

def main():
	path = sys.path[0]
	for parent, dirnames, filenames in os.walk(path):
		if parent == os.path.join(sys.path[0], 'out'):
			break
		for filename in filenames:
			if filename[-3:] in ['bmp', 'jpg', 'BMP', 'JPG']:
				get_text(parent, filename)
	print('已完成所有扫描。')

if __name__ == '__main__':
    main()
