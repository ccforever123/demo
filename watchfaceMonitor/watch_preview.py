import os
import re
from PIL import Image

def main():
    path = os.path.join(os.getcwd(), 'amazfit')
    watchfaceConfigFile = os.path.join(path, 'watchface/watch_face_config.xml')
    sourcePath = os.path.join(path, 'watchface/res')
    content = read_file(watchfaceConfigFile)
    dpi = int(get_dpi(content))
    widgetList = split_content(content)
    im = Image.new("RGBA", (dpi, dpi))
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


def read_file(filename):    # get file content
    with open(filename, 'r') as f:
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
    regWidgetType = re.compile(r'widget_type=\"(.*?)\".*?<(.*?)/>', re.S)
    widgetType, styleCode = regWidgetType.findall(widget)[0]
    styleDict = {}
    reg = re.compile(r'([a-zA-Z0-9_]*?)=\"(.*?)\"')
    styleList = reg.findall(styleCode)
    for styleKey, styleValue in styleList:
        styleDict[styleKey] = styleValue
    return widgetType, styleDict


def type_IMAGE(im, styleDict, sourcePath):
    resName = styleDict['res_name']
    x = int(styleDict['x'])
    y = int(styleDict['y'])
    imageFile = os.path.join(sourcePath, resName)
    img = Image.open(imageFile)
    r,g,b,a = img.split()
    im.paste(img, (x,y), mask=a)
    return im


def type_TEXTUREMAPPER(im, styleDict, sourcePath):
    pass


def type_CIRCLE(im, styleDict, sourcePath):
    pass


def type_LINE(im, styleDict, sourcePath):
    pass


def type_TEXTAREAWITHONEWILDCARD(im, styleDict, sourcePath):
    pass


def type_BOX(im, styleDict, sourcePath):
    pass


def type_SELECTIMAGE(im, styleDict, sourcePath):
    pass


def type_TEXTAREAWITHTWOWILDCARD(im, styleDict, sourcePath):
    pass




if __name__ == "__main__":
    main()