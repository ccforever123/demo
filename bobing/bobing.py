import logging
import random

#logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def result(list):
    count_1 = list.count(1)
    count_2 = list.count(2)
    count_3 = list.count(3)
    count_4 = list.count(4)
    count_5 = list.count(5)
    count_6 = list.count(6)
    if count_1 == count_2 == count_3 == count_4 == count_5 == count_6:
        return '对堂！'
    elif count_4 >= 4 or count_1 >= 5 or count_2 >= 5  or count_3 >= 5 or count_5 >= 5 or count_6 >= 5:
        return '状元！'
    elif count_4 == 3:
        return '三红！'
    elif count_4 == 2:
        return '二举！'
    elif count_4 == 1:
        return '一秀！'
    elif count_1 == 4 or count_2 == 4 or count_3 ==4 or count_5 == 4 or count_6 == 4:
        return '四进！'
    else:
        return 'Sorry！啥都没！'

def creat_list():
    list = [random.randint(1, 6) for i in range(6)]
    logging.debug(list)
    return list


if __name__ == '__main__':
    list = creat_list()
    result = result(list)
    print(result)

logging.debug('End of program')