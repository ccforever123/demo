import os, sys
import urllib.request
import logging
import threading
import time
#logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# https://blog.csdn.net/u014595019/article/details/48445223

def main():
    source_dict = get_source()
    code_list = get_code(source_dict)
    start(code_list)



def get_source():
    source_path = os.path.join(os.getcwd(), 'data\\source')
    source_dict = {}
    for parents, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            source  = os.path.join(source_path, filename)
            if filename == 'sh.csv':
                source_dict['0'] = source
            elif filename == 'sz.csv':
                source_dict['1'] = source
    return source_dict


def get_code(source_dict):
    code_list = []
    for locate in source_dict:
        with open(source_dict[locate], 'r') as f:
            content = f.readlines()
        while content != []:
            i = content.pop(0)
            code = locate + str(i.split(',')[0])
            if code[1:3] in ['00', '30', '60']:
                code_list.append(code)
            else:
                continue
    return code_list


def start(code_list):
    total = len(code_list)
    count = 1
    start_time = time.time()
    for code in code_list:
        file_path = os.path.join(sys.path[0], 'data\data\{}.csv'.format(code))
        if os.path.isfile(file_path) == False:
            download_data(file_path, code)
        proccess_bar(start_time, count, total)
        count += 1


def proccess_bar(start_time, count, total):
    count_time = time.time()
    caculate_time = count_time - start_time
    caculate_time_str = transfer_time(caculate_time)
    remaining_time = caculate_time / count * (total - count)
    remaining_time_str = transfer_time(remaining_time)
    percent = count / total
    process_bar = int(50 * percent) * '#'
    process_space = int(50 * (1 - percent)) * ' '

    output_info = '|{}{}| {} / {} - {:.2f}% | Cost: {}  Ramaining: {}'.format(process_bar, process_space, count,
                                                                                   total, percent * 100,
                                                                                   caculate_time_str,
                                                                                   remaining_time_str)
    output_final = output_info + ' ' * (148 - len(output_info))
    print(output_final, end='\r')


def transfer_time(seconds):
    if seconds > 60:
        caculate_time_m = seconds // 60
        if caculate_time_m > 60:
            caculate_time_h = caculate_time_m // 60
            caculate_time_m = caculate_time_m % 60
            caculate_time_s = seconds % 60
            caculate_time = '{:.0f}h{:.0f}m{:.2f}s'.format(caculate_time_h, caculate_time_m, caculate_time_s)
            return caculate_time
        else:
            caculate_time_s = seconds % 60
            caculate_time = '{:.0f}m{:.1f}s'.format(caculate_time_m, caculate_time_s)
    else:
        caculate_time = '{:.2f}s'.format(seconds)
    return caculate_time


def thread_download(code):
    pass


def download_data(file_path, code):
    try:
        # logging.debug('Downloading {}'.format(code))
        start_date = '20170104'
        end_date = '201801123'
        url = 'http://quotes.money.163.com/service/chddata.html?code={}&start={}&end={}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'.format(code, start_date, end_date)
        urllib.request.urlretrieve(url, file_path)
        # logging.debug('File Saved: {}'.format(data_path))
    except:
        time.sleep(1)
        download_data(code)





if __name__ == '__main__':
    main()


logging.debug('End of program')