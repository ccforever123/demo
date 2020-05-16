import os

def com(command):
    msg = os.popen('D:\\adb\\adb.exe {}'.format(command)).read()
    # print(msg)
    return msg