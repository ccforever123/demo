import os

def system_control(commamd):
    msg = os.popen('D:\\adb\\adb.exe {}'.format(commamd)).read()
    # print(msg)
    return msg


def device_control(deviceId, command):
    msg = os.popen('D:\\adb\\adb.exe -s {} {}'.format(deviceId, command)).read()
    # print(msg)
    return msg


if __name__ == "__main__":
    system_control('start-server')
    system_control('devices')
    system_control('kill-server')