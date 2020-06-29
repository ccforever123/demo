import formatTransfer
import os
from PIL import Image


def main():
    path = os.getcwd()
    for parents, dirnames, files in os.walk(path):
        for file in files:
            if file[-4:] == '.png':
                bmp2jpg(parents, file)


def bmp2jpg(path, filename):
    file_path = os.path.join(path, filename)
    img = Image.open(file_path)
    jpg_img = img.convert("RGB")
    target_file = os.path.join(path, 'output\\{}.jpg'.format(filename[:-4]))
    jpg_img.save(target_file)
    
 
if __name__ == "__main__":
    main()