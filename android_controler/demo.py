import adb

def get_deviceId():
    text = adb.com('devices')
    deviceId = (text.split('\t')[0]).split('\n')[1]
    deviceStatus = (text.split('\t')[1]).split('\n')[0]
    print(deviceId, deviceStatus)
    return deviceId, deviceStatus


def conn_device(deviceId, deviceStatus):
    if deviceStatus == 'device':
        conn = adb.com('shell pm list packages')
        print(conn)
    else:
        print('The device {} is {}'.format(deviceId, deviceStatus))


if __name__ == "__main__":
    start = adb.com('start-server')
    deviceId, deviceStatus = get_deviceId()
    conn_device(deviceId, deviceStatus)
    stop = adb.com('kill-server')