


def get_data_type(data_type):
    if data_type == 'DATA_STEPS':   # 步数值
        return '9999'
    elif data_type == 'DATA_CALORIE':   # 卡路里值
        return '999'
    elif data_type == 'DATA_HEARTRATE':   # 心率值
        return '199'
    elif data_type == 'DATA_STRENTHTIME':   # 中高强度时间
        return '99'
    elif data_type == 'DATA_TEMPERATURE':   # 温度值
        return '99'
    elif data_type == 'DATA_PM25':   # PM2.5
        return '99'
    elif data_type == 'DATA_AQI':   # AQI
        return '99'
    elif data_type == 'DATA_PRESSURE':   # 压力值
        return '99'
    elif data_type == 'DATA_AILTITUDE':   # 海拔高度
        return '99'
    elif data_type == 'DATA_POWER':   # 电量百分比值
        return '99'
    elif data_type == 'DATA_HOUR24':   # 24小时制小时
        return '12'
    elif data_type == 'DATA_HOUR12':   # 12小时制小时
        return '12'
    elif data_type == 'DATA_HOUR':   # 时
        return '12'
    elif data_type == 'DATA_MINITE':   # 分
        return '34'
    elif data_type == 'DATA_SECOND':   # 秒
        return '56'
    elif data_type == 'DATA_STANDUPTIMES':   # 站立时间
        return '99'
    elif data_type == 'DATA_VO2MAX':   # 最大摄氧量
        return '99'
    elif data_type == 'DATA_DATE':   # 日期
        return '19'
    elif data_type == 'DATA_HEARTRATE_MAX':   # 心率最大值
        return '99'
    elif data_type == 'DATA_HEARTRATE_MIN':   # 心率最小值
        return '99'
    elif data_type == 'DATA_AMPM':   # 12小时制时的上午/下午
        return 'AM'
    elif data_type == 'DATA_MONTH':   # 月份
        return '12'
    elif data_type == 'DATA_WEEK':   # 周
        return '1'
    elif data_type == 'DATA_WEATHERTYPE':   # 天气
        pass
    elif data_type == 'DATA_POWER_ENUM':   # 电量
        return '99'
    elif data_type == 'DATA_HOUR12_HIGH':   # 12小时制小时高位
        return '1'
    elif data_type == 'DATA_HOUR12_LOW':   # 12小时制小时低位
        return '2'
    elif data_type == 'DATA_HOUR24_HIGH':   # 24小时制小时高位
        return '1'
    elif data_type == 'DATA_HOUR24_LOW':   # 24小时制小时低位
        return '2'
    elif data_type == 'DATA_HOUR_HIGH':   # 小时高位
        return '1'
    elif data_type == 'DATA_HOUR_LOW':   # 小时低位
        return '2'
    elif data_type == 'DATA_MINITE_HIGH':   # 分钟高位
        return '3'
    elif data_type == 'DATA_MINITE_LOW':   #分钟低位 
        return '4'
    elif data_type == 'DATA_SECOND_HIGH':   # 秒数高位
        return '5'
    elif data_type == 'DATA_SECOND_LOW':   # 秒数低位
        return '6'
    elif data_type == 'DATA_STEPS_ONE':   # 步数个位
        return '9'
    elif data_type == 'DATA_STEPS_TWO':   # 步数十位
        return '9'
    elif data_type == 'DATA_STEPS_THREE':   # 步数百位
        return '9'
    elif data_type == 'DATA_STEPS_FOUR':   # 步数千位
        return '9'
    elif data_type == 'DATA_STEPS_FIVE':   # 步数万位
        return '9'
    elif data_type == 'DATA_DATE_HIGH':   # 日期高位
        return '2'
    elif data_type == 'DATA_DATE_LOW':   # 日期低位
        return '9'
    elif data_type == 'DATA_UNREADMSG_STATE':   # 未读消息状态
        pass
    elif data_type == 'DATA_HOUR12_RATIO':   # 12小时制小时数比例
        return '9'
    elif data_type == 'DATA_HOUR24_RATIO':   # 24小时制小时数比例
        return '9'
    elif data_type == 'DATA_HOUR_RATIO':   # 小时数比例
        return '9'
    elif data_type == 'DATA_MINITE_RATIO':   # 分钟数比例
        return '9'
    elif data_type == 'DATA_SECOND_RATIO':   # 秒数比例
        return '9'
    elif data_type == 'DATA_DATE_RATIO':   # 日期比例
        return '9'
    elif data_type == 'DATA_WEEK_RATIO':   # 周比例
        return '80'
    elif data_type == 'DATA_POWER_RATIO':   # 电量比例
        return '99'
    elif data_type == 'DATA_HEARTRATE_RATIO':   # 心率比例
        return '99'
    elif data_type == 'DATA_CALORIE_RATIO':   # 卡路里比例
        return '99'
    elif data_type == 'DATA_STANDUPTIMES_RATIO':   # 站立时间比例
        return '99'
    elif data_type == 'DATA_STRENTHTIME_RATIO':   # 中高强度时间比例
        return '99'
    elif data_type == 'DATA_STEPS_RATIO':   # 步数比例
        return '99'
    elif data_type == 'DATA_VO2MAX_RATIO':   # 最大摄氧量比例
        return '99'
    else:
        pass
    
