import time
import data_type
import random
import calendar

def init_data():
    now = get_time()
    heartrate = random.randint(0, 170)
    steps = random.randint(0, 65535)
    battery = random.randint(0, 100)
    calorie = random.randint(0, 65535)
    strenthtime = random.randint(0, 600)
    pm25 = random.randint(0, 100)
    aqi = random.randint(0, 100)
    pressure = random.randint(0, 100)
    standuptimes = random.randint(0, 20)
    vo2max = random.randint(0, 80)
    dataDict = {
        "DATA_HEARTRATE": heartrate,
        "DATA_STEPS": steps,
        "battery": battery,
        "DATA_CALORIE": calorie,
        "DATA_STRENTHTIME": strenthtime,
        "DATA_TEMPERATURE": random.randint(-20, 40),
        "DATA_PM25": pm25,
        "DATA_AQI": aqi,
        "DATA_PRESSURE": pressure,
        "DATA_AILTITUDE": random.randint(-100, 9999),    # 海拔高度
        "DATA_POWER": battery,   # 电量百分比值
        "DATA_HOUR24": now['hour'],
        "DATA_HOUR12": now['hour'],
        "DATA_HOUR": now['hour'],
        "DATA_MINITE": now['minute'],
        "DATA_SECOND": now['second'],
        "DATA_STANDUPTIMES": standuptimes,   # 站立次数
        "DATA_VO2MAX": vo2max,
        "DATA_DATE": now['date'],
        "DATA_HEARTRATE_MAX": heartrate + 20,
        "DATA_HEARTRATE_MIN": heartrate - 40,
        "DATA_AMPM": random.randint(0, 1),
        "DATA_MONTH": now['month'],
        "DATA_WEEK": now['week'],
        "DATA_WEATHERTYPE": random.randint(0, 11),
        "DATA_POWER_ENUM": int(battery / 10),    # 电量
        "DATA_HOUR12_HIGH": now['hourHigh'],
        "DATA_HOUR12_LOW": now['hourLow'],
        "DATA_HOUR24_HIGH": now['hourHigh'],
        "DATA_HOUR24_LOW": now['hourLow'],
        "DATA_HOUR_HIGH": now['hourHigh'],
        "DATA_HOUR_LOW": now['hourLow'],
        "DATA_MINITE_HIGH": now['minuteHigh'],
        "DATA_MINITE_LOW": now['minuteLow'],
        "DATA_SECOND_HIGH": now['secondHigh'],
        "DATA_SECOND_LOW": now['secondLow'],
        "DATA_STEPS_ONE": random.randint(0, 9),
        "DATA_STEPS_TWO": random.randint(0, 9),
        "DATA_STEPS_THREE": random.randint(0, 9),
        "DATA_STEPS_FOUR": random.randint(0, 9),
        "DATA_STEPS_FIVE": random.randint(0, 9),
        "DATA_DATE_HIGH": now['dateHigh'],
        "DATA_DATE_LOW": now['dateLow'],
        "DATA_UNREADMSG_STATE": random.randint(0, 1),
        "DATA_HOUR12_RATIO": now['hour'] / 12,
        "DATA_HOUR24_RATIO": now['hour'] / 24,
        "DATA_HOUR_RATIO": now['hour'] / 12,
        "DATA_MINITE_RATIO": now['minute'] / 60,
        "DATA_SECOND_RATIO": now['second'] / 60,
        "DATA_DATE_RATIO": now['date'] / 31,
        "DATA_WEEK_RATIO": now['week'] / 7,
        "DATA_POWER_RATIO": battery,  # 电量百分比
        "DATA_HEARTRATE_RATIO": heartrate / 1.7,
        "DATA_CALORIE_RATIO": calorie / 8000,
        "DATA_STANDUPTIMES_RATIO": standuptimes / 20, # 站立时间比例
        "DATA_STRENTHTIME_RATIO":  strenthtime / 600, # 中高强度时间比例
        "DATA_STEPS_RATIO": steps / 100,  # 步数比例
        "DATA_VO2MAX_RATIO":  vo2max / 80, # 最大摄氧量比例
        "DATA_NULL": '',
    }
    return dataDict


def get_time():
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
    return now


if __name__ == "__main__":
    init_data()