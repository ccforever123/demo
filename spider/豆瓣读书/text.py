# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image

def main():
	image = Image.open("captcha.jpg") #PIL loading pic
	#image.show()
	image = image.convert('RGBA') #convert to RGBA mode
	pix = image.load() #convert to pix mode
	for y in range(image.size[1]):
		for x in range(image.size[0]):
			if pix[x,y][0] < 95 or pix[x,y][1] <95 or pix[x,y][2] < 95:
				pix[x,y] = (0,0,0,255)
			else:
				pix[x,y] = (255,255,255,255)
	image.save('new_pic.bmp')


	text = pytesseract.image_to_string(image)
	#print(text)
	with open("output.txt", "w") as f:
		print(text)
		f.write(str(text))

if __name__ == '__main__':
    main()