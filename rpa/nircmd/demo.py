# encoding: utf-8
import os
import nircmd
import time

def main():
    exeFile = 'C:\ServYou\EPPortalXM_DS3.0_V2.1\EPEvenue_SH.exe'
    os.system(exeFile)
    print('starting the file: {}'.format(exeFile))
    time.sleep(5)
    # 选择申报密码登陆
    nircmd.set_cursor(1400, 580)
    time.sleep(1)
    nircmd.click()
    for i in range(0, 2):
        nircmd.set_cursor(1200, 640)
        nircmd.click()
        startYpx = 670
        ddd(startYpx)

        


def ddd(startYpx):
    nircmd.set_cursor(1200, startYpx)
    time.sleep(1)
    nircmd.click()
    print('click the mouse at (1200, {})'.format(startYpx))


if __name__ == "__main__":
    main()