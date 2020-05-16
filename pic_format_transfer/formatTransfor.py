from PIL import Image
import os
import argparse

def bmp2jpg(path, filename):
    file_path = os.path.join(path, filename)
    img = Image.open(file_path)
    img = img.transpose(Image.ROTATE_90)
    target_file = os.path.join(path, 'output\\pillow\\{}.jpg'.format(filename[:-4]))
    img.save(target_file)


# 逆时针旋转90度
def RotateAntiClockWise90(img):
    trans_img = cv2.transpose(img)
    new_img = cv2.flip(trans_img, 0)
    return new_img


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', type=str, default='', help='the path')
    parser.add_argument('--file', '-f', type=str, default='1.bmp', help='the file')
    opt = parser.parse_args()
    path = opt.path
    filename = opt.file
    outputPath = os.path.join(path, 'output')
    if os.path.isdir(outputPath) == False:
        os.mkdir(outputPath)
        os.mkdir(os.path.join(outputPath, 'pillow'))
        os.mkdir(os.path.join(outputPath, 'opencv'))
    for parents, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename[-3:] == 'png':
                bmp2jpg(path, filename)
                print('{} finished.'.format(filename))