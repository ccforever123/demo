import os,sys
import urllib.request

# 获取图片起始文件名
def get_current_img_num(path):
	img_path = os.path.join(path, 'img')
	for parent, dirnames, filenames in os.walk(img_path):
		print(filenames)
		if filenames == []:
			return '0'
		else:
			print(sorted(filenames))
			return sorted(filenames)[-1][:-4]

# 获取验证码图片
def get_verification_img(img_name, verification_path):
	url = 'http://oa.gwchina.cn/weaver/weaver.file.MakeValidateCode'
	urllib.request.urlretrieve(url, '%s%s.bmp' % (os.path.join(verification_path, 'img\\'), img_name))
	print('Downloading %s.jpg' % img_name)

def main():
	verification_path = sys.path[0]
	start_img_name = get_current_img_num(verification_path)
	img_name = int(start_img_name) + 1
	while True:
		get_verification_img(img_name, verification_path)
		img_name += 1

if __name__ == '__main__':
    main()
