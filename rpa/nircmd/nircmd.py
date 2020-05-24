import os

def save_screenshot_win(savePath):  # 激活窗户截图
    os.system('.\\nircmd.exe savescreenshotwin {}\\screenshotwin.png'.format(savePath))
    print('the screenshotwin has been saved into {}'.format(savePath))


def save_screenshot_full(savePath): # 全屏截图
    os.system('.\\nircmd.exe savescreenshotfull {}\\screenshotfull.png'.format(savePath))
    print('the screenshotfull has been saved into {}'.format(savePath))


def main():
    pass


if __name__ == "__main__":
    main()