# encoding: utf-8
import os

def save_screenshot_win(savePath):  # 激活窗户截图
    os.system('.\\nircmd.exe savescreenshotwin {}\\screenshotwin.png'.format(savePath))
    print('the screenshotwin has been saved into {}'.format(savePath))


def save_screenshot_full(savePath): # 全屏截图
    os.system('.\\nircmd.exe savescreenshotfull {}\\screenshotfull.png'.format(savePath))
    print('the screenshotfull has been saved into {}'.format(savePath))


def set_cursor(x, y):  # 移动光标（绝对位置）
    os.system('.\\nircmd.exe setcursor {} {}'.format(x, y))
    print('click the mouse at ({}, {})'.format(x, y))


def move_mouse(x, y):   # 移动鼠标（相对位置）
    os.system('.\\nircmd.exe sendmouse move {} {}'.format(x, y))
    print('click the mouse to ({}, {})'.format(x, y))


def click(side='left'):
    os.system('.\\nircmd.exe sendmouse {} click'.format(side))
    print('{} click'.format(side))


def double_click(side='left'):
    os.system('.\\nircmd.exe sendmouse {} dblclick'.format(side))
    print('{} double click}'.format(side))


def run_exe(exeFile, winMode='max'):
    os.system('.\\nircmd.exe exec {} {}'.format(exeFile, winMode))
    print('starting the file: {} with {}'.format(exeFile, winMode))


def main():
    pass


if __name__ == "__main__":
    main()
    set_cursor(480, 25)
    click()