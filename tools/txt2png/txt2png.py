import pygame
import os  
from PIL import Image, ImageFont, ImageDraw


def pygame_func():
    pygame.init()

    text = '水动乐西柚味运动饮料600ml'
    font = pygame.font.SysFont('simhei', 40)
    ftext = font.render(text, True, (0, 0, 0))
    pygame.image.save(ftext, "t.png")

    pygame.quit()


def Image_func():
    text = u"水动乐西柚味运动饮料600ml"
    im = Image.new("RGB", (520, 50), (255, 255, 255))  
    dr = ImageDraw.Draw(im)  
    font = ImageFont.truetype(("simhei"), 40)
    dr.text((10, 5), text, font=font, fill="#000000")
    # 拉伸图片
    img = im
    img.save("output\\{}.png".format(text))
    im = im.resize((200, 50),Image.ANTIALIAS)
    # 转化为灰度图
    imgry = im.convert('L')
    # 进入灰度阈值判断
    for threshold in range(10, 260, 10):
        table, threshold = get_bin_table(threshold)
        out = imgry.point(table, '1')
        # out.show()  
        out.save("output\\{}.png".format(threshold))

def get_bin_table(threshold = 100):
    # 获取灰度转二值的映射table
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table, threshold


if __name__ == "__main__":
    # pygame_func()
    Image_func()