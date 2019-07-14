from PIL import Image
import os
import math

def create_ring(dataType, resName, sourcePath, x, y, bigR, smallR, arcStart, arcEnd, data):
    imageFile = os.path.join(sourcePath, resName)
    img = Image.open(imageFile).convert('RGBA')
    width, height = img.size
    # 切出大圆
    bigCircle = img
    for i in range(width):
        for j in range(height):
            a, b = (i - x), (j - y)
            distance = pythagorean_theorem(a, b)
            if distance > bigR:
                bigCircle.putpixel((i,j), (0,0,0,0))
    r,g,b,a = img.split()
    img.paste(bigCircle, (0,0), mask=a)
    # 切出小圆，黏贴形成圆环
    for i in range(width):
        for j in range(height):
            a, b = (i - x), (j - y)
            distance = pythagorean_theorem(a, b)
            if distance < smallR:
                img.putpixel((i,j), (0,0,0,0))
    smallCircle = img
    r,g,b,a = img.split()
    img.paste(smallCircle, (0,0), mask=a)

    # 判断旋转角度
    # logs = []
    arcMax = max(arcStart, arcEnd)
    arcMin = min(arcStart, arcEnd)
    arcData = data * 0.01 * (arcMax - arcMin)   # 获取数据在Circle中的占比值
    print('dataType={}, arcRange={}-{}, arcData={}%={}'.format(dataType, arcStart, arcEnd, data, arcData))
    if arcStart < arcEnd:
        arcMax = min(arcMax, arcMin + arcData)
    else:
        arcMin = max(arcMin, arcMax - arcData)
    for i in range(width):
        for j in range(height):  
            a, b = (i - x), (y - j)
            if a != 0:
                degree = math.degrees(math.atan(b / a))
                if a < 0 and b > 0: # 第四象限
                    degree = 270 - degree
                elif a < 0 and b < 0:   # 第三象限
                    degree = 270 - degree
                elif a > 0 and b > 0:   #第一象限
                    degree = 90 - degree
                else:    # 第二象限
                    degree = 90 - degree
                if degree < arcMin or degree > arcMax:
                    # text = "-> ({}, {}), degree: {:.0f}, range: {}-{}\n".format(a, b, degree, arcMin, arcMax)
                    # logs.append(text)
                    img.putpixel((i,j), (0,0,0,0))
                # else:
                #     text = " × ({}, {}), degree: {:.0f}, range: {}-{}\n".format(a, b, degree, arcMin, arcMax)
                #     logs.append(text)
            else:
                img.putpixel((i,j), (0,0,0,0))
    # with open('log.txt', 'w', encoding='utf-8') as f:
    #     for text in logs:
    #         f.write(text)
    r,g,b,a = img.split()
    img.paste(smallCircle, (0,0), mask=a)

    r,g,b,a = img.split()
    return img, a


def pythagorean_theorem(a, b):
    return (a**2 + b**2)**0.5