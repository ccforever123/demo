import os
import re
from PIL import Image, ImageDraw, ImageFont
from data_type import get_data_type, get_data_angle
from font_type import get_font_type
from data_connector_type import get_connector_type
import time
import calendar
import random
from matplotlib.patches import Circle 
import math
# import cv2
# import numpy as np

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(now)
dayStr, timeStr = now.split(' ')
year, month, date = dayStr.split('-')
hour, minute, second = timeStr.split(':')
week = calendar.weekday(int(year), int(month), int(date)) + 1
if len(date) < 2:
    date = '0' + date
dateHigh, dateLow = date[0], date[1]
if len(hour) < 2:
    hour = '0' + hour
hourHigh, hourLow = hour[0], hour[1]
if len(minute) < 2:
    minute = '0' + minute
minuteHigh, minuteLow = minute[0], minute[1]
if len(second) < 2:
    second = '0' + second
secondHigh, secondLow = second[0], second[1]
now = {
    "month": int(month),
    "date": int(date),
    "dateHigh": int(dateHigh),
    "dateLow": int(dateLow),
    "hour": int(hour),
    "hourHigh": int(hourHigh),
    "hourLow": int(hourLow),
    "minute": int(minute),
    "minuteHigh": int(minuteHigh),
    "minuteLow": int(minuteLow),
    "second": int(second),
    "secondHigh": int(secondHigh),
    "secondLow": int(secondLow),
    "week": int(week)
}


def main():
    path = os.path.join(os.getcwd(), 'custom_ch')
    watchfaceConfigFile = os.path.join(path, 'watchface\\watch_face_config.xml')
    sourcePath = os.path.join(path, 'watchface\\res')
    content = read_file(watchfaceConfigFile)
    dpi = int(get_dpi(content))
    widgetList = split_content(content)
    im = Image.new("RGBA", (dpi, dpi))  # a new image, size = dpi
    for widget in widgetList:
        widgetType, styleDict = seperate_widget_type(widget)
        if widgetType == 'IMAGE':
            im = type_IMAGE(im, styleDict, sourcePath)
        elif widgetType == 'TEXTUREMAPPER':
            im = type_TEXTUREMAPPER(im, styleDict, sourcePath)
        elif widgetType == 'CIRCLE':
            im = type_CIRCLE(im, styleDict, sourcePath)
        elif widgetType == 'LINE':
            im = type_LINE(im, styleDict, sourcePath)
        elif widgetType == 'TEXTAREAWITHONEWILDCARD':
            im = type_TEXTAREAWITHONEWILDCARD(im, styleDict, sourcePath)
        elif widgetType == 'BOX':
            im = type_BOX(im, styleDict, sourcePath)
        elif widgetType == 'SELECTIMAGE':
            im = type_SELECTIMAGE(im, styleDict, sourcePath)
        elif widgetType == 'TEXTAREAWITHTWOWILDCARD':
            im = type_TEXTAREAWITHTWOWILDCARD(im, styleDict, sourcePath)
        else:
            print('Error: Missing the widget type: {}'.format(widgetType))
    im.show()


def read_file(filename):    # get file content
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def get_dpi(content):
    regDpi = re.compile(r'<TemplateWatch dpi=\"(.*?)\">')
    dpi = regDpi.findall(content)[0]
    return dpi


def split_content(content): # split the content with <widget>
    regWidget = re.compile(r'(<Widget.*?</Widget>)', re.S)
    widgetList = regWidget.findall(content)
    return widgetList


def seperate_widget_type(widget):    # seperate the widget type
    regWidgetType = re.compile(r'widget_type=\"(.*?)\"', re.S)
    widgetType = regWidgetType.findall(widget)[0]
    styleDict = {}
    reg = re.compile(r'([a-zA-Z0-9_]*?)=\"(.*?)\"')
    styleList = reg.findall(widget)
    for styleKey, styleValue in styleList:
        styleDict[styleKey] = styleValue
    return widgetType, styleDict


def open_image(resName, sourcePath):    # open the source image and return the rbga format pic, mask=a
    imageFile = os.path.join(sourcePath, resName)
    # img = cv2.imread(imageFile, 0)
    img = Image.open(imageFile)
    r,g,b,a = img.split()
    return img, a


def type_IMAGE(im, styleDict, sourcePath):  # 静态图，如背景图、图标等
    resName = styleDict['res_name'] # 引用的图片ID
    x = int(styleDict['x']) # 图片左上角X坐标
    y = int(styleDict['y']) # 图片左上角Y坐标
    img, a = open_image(resName, sourcePath)
    im.paste(img, (x,y), mask=a)
    return im


def type_TEXTUREMAPPER(im, styleDict, sourcePath):  # 图片旋转，如时分秒针等
    resName = styleDict['res_name'] # 引用的图片ID
    drawableX = int(styleDict['drawable_x'])    # 图片旋转绘制区域左上角X坐标
    drawableY = int(styleDict['drawable_y'])    # 图片旋转绘制区域左上角Y坐标
    drawableWidth = int(styleDict['drawable_width'])    # 图片旋转绘制区域宽度
    drawableHeight = int(styleDict['drawable_height'])  # 图片旋转绘制区域高度
    rotationCenterX = int(styleDict['rotation_center_x'])  # 旋转中心在图片上的x坐标
    rotationCenterY = int(styleDict['rotation_center_y'])  # 旋转中心在图片上的y坐标
    beginArc = int(styleDict['begin_arc'])  # 旋转起始角度
    endArc = int(styleDict['end_arc'])  # 旋转终止角度
    dataType = styleDict['data_type']  # 数据类型

    # 新建一个覆盖了指针旋转的方形大图，避免旋转时指针被裁切，大图的长宽均为2*rotationCenterY
    img, a = open_image(resName, sourcePath)
    imgWidth, imgHeight = img.size
    newDpi = 2 * rotationCenterY
    newImg = Image.new("RGBA", (newDpi, newDpi))
    newImgWidth, newImgHeight = newImg.size
    newX = int((newDpi - imgWidth) / 2)
    newY = int(newImgWidth / 2 - rotationCenterY)

    newImg.paste(img, (newX, newY), mask=a) # 黏贴好指针后，将背景设为透明 

    # 指针旋转
    # angle = random.randint(beginArc, endArc)
    data = get_data_type(dataType, now)
    # dataAngle = get_data_angle(dataType, data)
    angle = data * (endArc - beginArc) + beginArc
    # print('dataType={}, data={:.2f}, angleRange={}-{}, angle={:.2f}'.format(dataType, data, beginArc, endArc, angle))
    newImg = newImg.rotate(-angle)

    
    # 重新对指针放置坐标进行定位
    x = int(drawableWidth / 2 - rotationCenterX) - newX
    y = int(drawableHeight / 2 - rotationCenterY)
    # print('im.size={}, x={}, y={}, newImg.size={}'.format(im.size, x, y, newImg.size))
    r,g,b,alpha = newImg.split()   
    im.paste(newImg, (x,y), mask=alpha)
    return im


def type_CIRCLE(im, styleDict, sourcePath): # 圆形进度条，用于步数、卡路里等的目标完成进度显示
    resName = styleDict['res_name'] # 引用的图片ID
    drawableX = int(styleDict['drawable_x'])    # 控件左上角X坐标
    drawableY = int(styleDict['drawable_y'])    # 控件左上角Y坐标
    drawableWidth = int(styleDict['drawable_width'])    # 图片旋转绘制区域宽度
    drawableHeight = int(styleDict['drawable_height'])  # 图片旋转绘制区域高度
    circleX = int(styleDict['circle_x'])    # 圆形进度条的圆心位置X坐标
    circleY = int(styleDict['circle_y'])    # 圆形进度条的圆心位置X坐标
    circleR = int(styleDict['circle_r'])    # 圆形进度条的半径
    lineWidth = int(styleDict['line_width'])    # 圆形进度条的宽度
    arcStart = int(styleDict['arc_start'])    # 圆形进度条范围的起始角度
    arcEnd = int(styleDict['arc_end'])    # 圆形进度条范围的结束角度
    updateArcStart = int(styleDict['update_arc_start'])    # 圆形进度条的默认角度
    precision = int(styleDict['precision'])    # 设置Circle绘制功能的精度。精度是以度为单位的，默认值为5，值越高，圆圈步进越大，但渲染速度越快。
    dataType = styleDict['data_type']    # 订阅的数据

    # 画出圆环中的大圆和小圆，并透明化圆外区域
    bigR = circleR + lineWidth / 2
    smallR = circleR - lineWidth / 2
    
    img, a = create_ring(resName, sourcePath, circleX, circleY, bigR, smallR, arcStart, arcEnd)

    # img, a = open_image(resName, sourcePath)
    im.paste(img, (drawableX,drawableY), mask=a)
    
    return im


def type_LINE(im, styleDict, sourcePath):   # 线形进度条，用于步数、卡路里等的目标完成进度显示
    resName = styleDict['res_name'] # 引用的图片ID
    drawableX = int(styleDict['drawable_x'])    # 控件左上角X坐标
    drawableY = int(styleDict['drawable_y'])    # 控件左上角Y坐标
    drawableWidth = int(styleDict['drawable_width'])    # 控件宽度
    drawableHeight = int(styleDict['drawable_height'])  # 控件高度
    dataType = styleDict['data_type']    # 订阅的数据

    return im


def type_TEXTAREAWITHONEWILDCARD(im, styleDict, sourcePath):    # 动态文本框，用于显示变化的文字，如步数、心率等的数值
    drawableX = int(styleDict['drawable_x'])    # 文本框左上角X坐标
    drawableY = int(styleDict['drawable_y'])    # 文本框左上角Y坐标
    drawableWidth = int(styleDict['drawable_width'])    # 文本框宽度
    drawableHeight = int(styleDict['drawable_height'])  # 文本框高度
    dataType = styleDict['data_type']    # 订阅的数据
    colorRed = int(styleDict['color_red'])    # 文本颜色的红色分量值
    colorGreen = int(styleDict['color_green'])    # 文本颜色的绿色分量值
    colorBlue = int(styleDict['color_blue'])    # 文本颜色的蓝色分量值
    lineSpacing = int(styleDict['line_spacing'])    # 行间距
    alignmentType = styleDict['alignment_type']    # 对齐方式(LEFT或CENTER或RIGHT)
    fontType = styleDict['font_type']    # 字体字号
    alpha = int(styleDict['alpha'])    # 文本的透明度值

    data = get_data_type(dataType, now)
    fontFile, fontsize = get_font_type(fontType)
    font = ImageFont.truetype(fontFile, fontsize)
    ImageDraw.Draw(im).text((drawableX, drawableY), str(data), (colorRed, colorGreen, colorBlue), font=font)

    return im


def type_BOX(im, styleDict, sourcePath):    # 背景框，用于显示背景色
    drawableX = int(styleDict['drawable_x'])    # 背景框左上角X坐标
    drawableY = int(styleDict['drawable_y'])    # 背景框左上角Y坐标
    drawableWidth = int(styleDict['drawable_width'])    # 背景框宽度
    drawableHeight = int(styleDict['drawable_height'])  # 背景框高度
    colorRed = int(styleDict['color_red'])    # 文本颜色的红色分量值
    colorGreen = int(styleDict['color_green'])    # 文本颜色的绿色分量值
    colorBlue = int(styleDict['color_blue'])    # 文本颜色的蓝色分量值

    return im


def type_SELECTIMAGE(im, styleDict, sourcePath):    # 随着订阅的数据类型的数据改变，显示不同的图片
    drawableX = int(styleDict['drawable_x'])    # 文本框左上角X坐标
    drawableY = int(styleDict['drawable_y'])    # 文本框左上角Y坐标
    dataType = styleDict['data_type']    # 订阅的数据
    res0 = styleDict['res_0']  # 序列帧第1幅图片ID
    res1 = styleDict['res_1']  # 序列帧第2幅图片ID
    res2 = styleDict['res_2']  # 序列帧第3幅图片ID
    res3 = styleDict['res_3']  # 序列帧第4幅图片ID
    res4 = styleDict['res_4']  # 序列帧第5幅图片ID
    res5 = styleDict['res_5']  # 序列帧第6幅图片ID
    res6 = styleDict['res_6']  # 序列帧第7幅图片ID
    res7 = styleDict['res_7']  # 序列帧第8幅图片ID
    res8 = styleDict['res_8']  # 序列帧第9幅图片ID
    res9 = styleDict['res_9']  # 序列帧第10幅图片ID
    res10 = styleDict['res_10']  # 序列帧第11幅图片ID
    res11 = styleDict['res_11']  # 序列帧第12幅图片ID
    res12 = styleDict['res_12']  # 序列帧第13幅图片ID
    res13 = styleDict['res_13']  # 序列帧第14幅图片ID
    res14 = styleDict['res_14']  # 序列帧第15幅图片ID
    resList = [res0, res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13, res14]
    resIndex = int(get_data_type(dataType, now))
    img, a = open_image(resList[resIndex], sourcePath)
    im.paste(img, (drawableX, drawableY), mask=a)

    return im


def type_TEXTAREAWITHTWOWILDCARD(im, styleDict, sourcePath):    # 带连接符的动态文本框，如：XX:XX格式的时间显示，XX/XX格式的日期显示。
    drawableX = int(styleDict['drawable_x'])    # 文本框左上角X坐标
    drawableY = int(styleDict['drawable_y'])    # 文本框左上角Y坐标
    drawableWidth = int(styleDict['drawable_width'])    # 文本框宽度
    drawableHeight = int(styleDict['drawable_height'])  # 文本框高度
    colorRed = int(styleDict['color_red'])    # 文本颜色的红色分量值
    colorGreen = int(styleDict['color_green'])    # 文本颜色的绿色分量值
    colorBlue = int(styleDict['color_blue'])    # 文本颜色的蓝色分量值
    dataType = styleDict['data_type']    # 订阅的数据
    data2Type = styleDict['data2_type']    # 订阅的数据
    lineSpacing = int(styleDict['line_spacing'])    # 行间距
    dataCconnectorType = styleDict['data_connector_type']    # 两个数据之间的连接符
    alignmentType = styleDict['alignment_type']    # 对齐方式(LEFT或CENTER或RIGHT)
    fontType = styleDict['font_type']    # 字体字号
    alpha = int(styleDict['alpha'])    # 文本的透明度值

    dataConnector = get_connector_type(dataCconnectorType)
    data = str(get_data_type(dataType, now)) + dataConnector + str(get_data_type(data2Type, now))
    fontFile, fontsize = get_font_type(fontType)
    font = ImageFont.truetype(fontFile, fontsize)

    ImageDraw.Draw(im).text((drawableX, drawableY), str(data), (colorRed, colorGreen, colorBlue), font=font)

    return im


def create_ring(resName, sourcePath, x, y, bigR, smallR, arcStart, arcEnd):
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
    texts = []
    for i in range(width):
        for j in range(height):  
            a, b = (i - x), (j - y)
            if a != 0:
                degree = math.degrees(math.atan(b / a))
                if degree < 0:
                    degree = degree
                if degree < arcStart or degree > arcEnd:
                    text = "-> ({}, {}), degree: {}, range: {}-{}\n".format(a, b, degree, arcStart, arcEnd)
                    texts.append(text)
                    print(text[:-1])
                    with open('log.txt', 'a', encoding='utf-8') as f:
                        f.write(text[:-1])
                    img.putpixel((i,j), (0,0,0,0))
                else:
                    text = " × ({}, {}), degree: {}, range: {}-{}\n".format(a, b, degree, arcStart, arcEnd)
                    texts.append(text)
                    print(text[:-1])
                
            else:
                img.putpixel((i,j), (0,0,0,0))
    with open('log.txt', 'w', encoding='utf-8') as f:
        for text in texts:
            f.write(text)
    r,g,b,a = img.split()
    img.paste(smallCircle, (0,0), mask=a)



    r,g,b,a = img.split()
    return img, a


def pythagorean_theorem(a, b):
    return (a**2 + b**2)**0.5



if __name__ == "__main__":
    main()