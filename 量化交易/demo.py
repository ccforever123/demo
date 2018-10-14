import matplotlib.pyplot as plt
import os
from pylab import *
import logging
mpl.rcParams['font.sans-serif'] = ['SimHei']

def get_file():
    path = os.path.join(os.getcwd(), 'data/data')
    filename = os.path.join(path, '1000725.csv')
    data = get_data(filename)
    draw(filename, data)

def get_data(filename):
    data = {
        'date': [],
        'id': [],
        'name': [],
        'end': [],
        'high': [],
        'low': [],
        'begin': [],
        'yesterday': [],
        'change': [],
        'rate': [],
        'vol': [],
        'total': []
    }
    with open(filename, 'r') as f:
        content = f.readlines()
    content.reverse()
    for i in content[-300:-1]:

        date = i.split(',')[0]
        id = i.split(',')[1]
        name = i.split(',')[2]
        end = float(i.split(',')[3])
        high = float(i.split(',')[4])
        low = float(i.split(',')[5])
        begin = float(i.split(',')[6])
        yesterday = float(i.split(',')[7])
        if i.split(',')[8] == 'None':
            data['date'].append(date)
            data['id'].append(id)
            data['name'].append(name)
            data['end'].append(end)
            data['high'].append(high)
            data['low'].append(low)
            data['begin'].append(begin)
            data['yesterday'].append(yesterday)
            data['change'].append(0)
            data['rate'].append(0)
            data['vol'].append(0)
            data['total'].append(0)
            continue
        change = float(i.split(',')[8])
        rate = float(i.split(',')[9])
        vol = float(i.split(',')[10])
        total = float(i.split(',')[11])
        print(i[:-1])

        data['date'].append(date)
        data['id'].append(id)
        data['name'].append(name)
        data['end'].append(end)
        data['high'].append(high)
        data['low'].append(low)
        data['begin'].append(begin)
        data['yesterday'].append(yesterday)
        data['change'].append(change)
        data['rate'].append(rate)
        data['vol'].append(vol)
        data['total'].append(total)
    return data

def draw(filename, data):
    logging.debug('图片生成中...')
    fig = plt.figure(figsize=(30, 18), dpi=80)
    name = data['name'][0]
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(data['date'], data['end'], label='price', color='red')
    ax1.set_xlabel('date')
    ax1.set_ylabel('price')
    ax1.set_title('{} - {}'.format(filename, name))
    ax1.legend()

    ax2 = ax1.twinx()
    ax2.bar(data['date'], data['vol'], label='vol', color='blue')
    ax2.set_ylabel('vol')
    ax2.legend()
    # plt.title('{} - {}'.format(filename, name))


    logging.debug('请稍等...')
    plt.show()
    logging.debug('图片生成完成')

if __name__ == '__main__':
    get_file()