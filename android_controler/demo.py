# -*- coding:utf8 -*-
import adb

# 获取当前连接的设备id和状态
def get_deviceId():
    text = adb.system_ctrl('devices')
    devices = text.split('\n')
    for i in range(len(devices)):
        print('{}: {}'.format(i, devices[i]))
    choose = input('Pls choose the device:')
    selected = devices[int(choose)]
    deviceId = selected.split('\t')[0]
    deviceStatus = (selected.split('\t')[1]).split('\n')[0]
    print(text)
    return deviceId, deviceStatus


# 查看当前前台运行的Activity
def conn_device(deviceId, deviceStatus):
    if deviceStatus == 'device':
        print('The device {} is now been connected.'.format(deviceId))
        comm = 'shell "dumpsys activity activities | grep mResumedActivity"'
        conn = adb.device_ctrl(deviceId, comm)
        print(conn)
    else:
        print('The device {} is {}'.format(deviceId, deviceStatus))



# 启动指定Activity
def start_app(deviceId):
    appActivity = 'com.pingan.lifeinsurance'
    comm = 'shell am start -n {}'.format(deviceId, appActivity)
    run = adb.device_ctrl(deviceId, comm)
    print(run)


if __name__ == "__main__":
    start = adb.system_ctrl('start-server')
    deviceId, deviceStatus = get_deviceId()
    conn_device(deviceId, deviceStatus)
    start_app(deviceId)
    stop = adb.system_ctrl('kill-server')