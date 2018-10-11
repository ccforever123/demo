import os, sys
import requests
import urllib.request
import logging
import threading
import time
#logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

# https://blog.csdn.net/u014595019/article/details/48445223

def read_file(code_file, file):
    if code_file == 'sh.csv':
        locate_id = '0'
    else:
        locate_id = '1'
    with open(file, 'r') as f:
        content = f.readlines()
        '''
    for i in content:
        code = locate_id + str(i.split(',')[0])
        get_source(code)
        '''
    while content != []:
        i = content.pop(0)
        code = locate_id + str(i.split(',')[0])
        if code[1:3] in ['00', '30', '60']:
            t = threading.Thread(target=get_source, args=(code,))
            t.start()
            time.sleep(0.05)


def get_source(code):
    logging.debug('Downloading {}'.format(code))
    data_path = os.path.join(sys.path[0], 'data\data\{}.csv'.format(code))
    url = 'http://quotes.money.163.com/service/chddata.html?code={}&start=20100104&end=20180928&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'.format(code)
    urllib.request.urlretrieve(url, data_path)
    logging.debug('File Saved: {}'.format(data_path))


def download_data():
    data_path = os.path.join(sys.path[0], 'data\source')
    code_file_list = ['sh.csv', 'sz.csv']
    for code_file in code_file_list:
        file = os.path.join(data_path, code_file)
        read_file(code_file, file)


if __name__ == '__main__':
    download_data()


logging.debug('End of program')