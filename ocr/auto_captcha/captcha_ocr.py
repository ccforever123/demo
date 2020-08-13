from PIL import Image
import pytesseract
import os
import shutil

def captcha_ocr(folder, filename):
    cutFolder = os.path.join(folder, 'cut')
    # if os.path.isdir(cutFolder):
    #     shutil.rmtree(cutFolder)
    if os.path.isdir(cutFolder) == False:
        os.mkdir(cutFolder)
    codes = cut(folder, filename)
    filePath = os.path.join(folder, filename)
    targetPath = os.path.join(folder, '{}.bmp'.format(codes))
    print('{} -> {}'.format(filename, codes))
    os.rename(filePath, targetPath)

def cut(folder, filename):
    imgPath = os.path.join(folder, filename)
    savePath = os.path.join(folder, 'cut')
    image = Image.open(imgPath)
    width, height = image.size
    cut_x = [0, 32, 47, 60]
    code_list = []
    for i in range(len(cut_x)):
        x = cut_x[i]
        if i < len(cut_x) - 1:
            itemWidth = cut_x[i+1] - cut_x[i]
        else:
            itemWidth = 80 - cut_x[i]
        new_image = Image.new('RGBA', (itemWidth, height), 'white')
        new_image.paste(image, (-x,0))
        new_filename = '{}_{}.bmp'.format(filename.split('.')[0], i)
        new_image.save(os.path.join(savePath, new_filename))
        code = ocr(savePath, new_filename)
        code_list.append(code)
    codes = ''.join(code_list)
    return codes


def ocr(folder, filename):
    imgPath = os.path.join(folder, filename)
    imgCaptcha = Image.open(imgPath).convert('RGBA')
    image = imgCaptcha.rotate(25)
    new_image = Image.new('RGBA', image.size, 'white')
    image = Image.composite(image, new_image, image)
    imgry = image.convert('L')  # 转化为灰度图
    table = get_bin_table()
    out = imgry.point(table, '1')
    code = pytesseract.image_to_string(out, lang='eng', config='--oem 0 -psm 10 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    outFolder = os.path.join(folder, 'out')
    if os.path.isdir(outFolder) == False:
        os.mkdir(outFolder)
    out.save(os.path.join(folder, 'out', filename))
    return code


def get_bin_table(threshold = 140):
    # 获取灰度转二值的映射table
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


if __name__ == "__main__":
    folder = os.path.join(os.getcwd(), 'img')
    cutFolder = os.path.join(folder, 'cut')
    if os.path.isdir(cutFolder):
        shutil.rmtree(cutFolder)
    for parents, dirnames, filenames in os.walk(folder):
        if parents == folder:
            for filename in filenames:
                captcha_ocr(folder, filename)
                # if code != '':
                #     newName = os.path.join(folder, 'out', '{}.bmp'.format(code))
                #     os.rename(os.path.join(folder, 'out', filename), newName)