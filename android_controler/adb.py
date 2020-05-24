import os

def system_ctrl(commamd):
    msg = os.popen('D:\\adb\\adb.exe {}'.format(commamd)).read()
    # print(msg)
    return msg


def device_ctrl(deviceId, command):
    msg = os.popen('D:\\adb\\adb.exe -s {} {}'.format(deviceId, command)).read()
    # print(msg)
    return msg


if __name__ == "__main__":
    system_ctrl('start-server')
    system_ctrl('devices')
    system_ctrl('kill-server')