import random


def get_data_type(data_type, now):
    if data_type == 'DATA_STEPS':   # 步数值
        return random.randint(0, 65535)
    elif data_type == 'DATA_CALORIE':   # 卡路里值
        return random.randint(0, 65535)
    elif data_type == 'DATA_HEARTRATE':   # 心率值
        return random.randint(0, 255)
    elif data_type == 'DATA_STRENTHTIME':   # 中高强度时间
        return random.randint(0, 65535)
    elif data_type == 'DATA_TEMPERATURE':   # 温度值
        return random.randint(-32678, 32678)
    elif data_type == 'DATA_PM25':   # PM2.5
        return random.randint(0, 500)
    elif data_type == 'DATA_AQI':   # AQI
        return random.randint(0, 500)
    elif data_type == 'DATA_PRESSURE':   # 气压值
        return random.randint(0, 65535)
    elif data_type == 'DATA_AILTITUDE':   # 海拔高度
        return random.randint(-32678, 32678)
    elif data_type == 'DATA_POWER':   # 电量百分比值
        return random.randint(0, 100)
    elif data_type == 'DATA_HOUR24':   # 24小时制小时
        return now['hour']
    elif data_type == 'DATA_HOUR12':   # 12小时制小时
        return random.randint(0, 11)
    elif data_type == 'DATA_HOUR':   # 时
        return random.randint(0, 23)
    elif data_type == 'DATA_MINITE':   # 分
        return random.randint(0, 59)
    elif data_type == 'DATA_SECOND':   # 秒
        return random.randint(0, 59)
    elif data_type == 'DATA_STANDUPTIMES':   # 站立次数
        return random.randint(0, 255)
    elif data_type == 'DATA_VO2MAX':   # 最大摄氧量
        return random.randint(0, 80)
    elif data_type == 'DATA_DATE':   # 日期
        return now['date']
    elif data_type == 'DATA_HEARTRATE_MAX':   # 心率最大值
        return random.randint(0, 255)
    elif data_type == 'DATA_HEARTRATE_MIN':   # 心率最小值
        return random.randint(0, 255)
    elif data_type == 'DATA_AMPM':   # 12小时制时的上午/下午
        return random.randint(0, 1)
    elif data_type == 'DATA_MONTH':   # 月份
        return now['month']
    elif data_type == 'DATA_WEEK':   # 周
        return now['week']
    elif data_type == 'DATA_WEATHERTYPE':   # 天气
        return random.randint(0, 11)
    elif data_type == 'DATA_POWER_ENUM':   # 电量
        return random.randint(0, 10)
    elif data_type == 'DATA_HOUR12_HIGH':   # 12小时制小时高位
        return now['hourHigh']
    elif data_type == 'DATA_HOUR12_LOW':   # 12小时制小时低位
        return now['hourLow']
    elif data_type == 'DATA_HOUR24_HIGH':   # 24小时制小时高位
        return now['hourHigh']
    elif data_type == 'DATA_HOUR24_LOW':   # 24小时制小时低位
        return now['hourLow']
    elif data_type == 'DATA_HOUR_HIGH':   # 小时高位
        return now['hourHigh']
    elif data_type == 'DATA_HOUR_LOW':   # 小时低位
        return now['hourLow']
    elif data_type == 'DATA_MINITE_HIGH':   # 分钟高位
        return now['minuteHigh']
    elif data_type == 'DATA_MINITE_LOW':   #分钟低位 
        return now['minuteLow']
    elif data_type == 'DATA_SECOND_HIGH':   # 秒数高位
        return now['secondHigh']
    elif data_type == 'DATA_SECOND_LOW':   # 秒数低位
        return now['secondLow']
    elif data_type == 'DATA_STEPS_ONE':   # 步数个位
        return random.randint(0, 9)
    elif data_type == 'DATA_STEPS_TWO':   # 步数十位
        return random.randint(0, 9)
    elif data_type == 'DATA_STEPS_THREE':   # 步数百位
        return random.randint(0, 9)
    elif data_type == 'DATA_STEPS_FOUR':   # 步数千位
        return random.randint(0, 9)
    elif data_type == 'DATA_STEPS_FIVE':   # 步数万位
        return random.randint(0, 9)
    elif data_type == 'DATA_DATE_HIGH':   # 日期高位
        return now['dateHigh']
    elif data_type == 'DATA_DATE_LOW':   # 日期低位
        return now['dateLow']
    elif data_type == 'DATA_UNREADMSG_STATE':   # 未读消息状态
        return random.randint(0, 1)
    elif data_type == 'DATA_HOUR12_RATIO':   # 12小时制小时数比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_HOUR24_RATIO':   # 24小时制小时数比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_HOUR_RATIO':   # 小时数比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_MINITE_RATIO':   # 分钟数比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_SECOND_RATIO':   # 秒数比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_DATE_RATIO':   # 日期比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_WEEK_RATIO':   # 周比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_POWER_RATIO':   # 电量比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_HEARTRATE_RATIO':   # 心率比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_CALORIE_RATIO':   # 卡路里比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_STANDUPTIMES_RATIO':   # 站立时间比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_STRENTHTIME_RATIO':   # 中高强度时间比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_STEPS_RATIO':   # 步数比例
        return '{}%'.format(random.randint(0, 100))
    elif data_type == 'DATA_VO2MAX_RATIO':   # 最大摄氧量比例
        return '{}%'.format(random.randint(0, 100))
    else:
        return ''
