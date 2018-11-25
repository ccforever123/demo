import os
from datetime import datetime



def main():
    code = '0000001'
    gen_data(code)


def gen_data(code):
    new_content_list = []
    file_path = os.path.join(os.getcwd(), 'data\\data\\{}.csv'.format(code))
    train_path = os.path.join(os.getcwd(), 'data\\train.txt')
    test_path = os.path.join(os.getcwd(), 'data\\test.txt')
    with open(file_path, 'r') as f:
        content = f.readlines()
    for line in range(len(content)-6, 0, -1):
        i0 = content[line]
        i1 = content[line+1]
        i2 = content[line+2]
        i3 = content[line+3]
        i4 = content[line+4]
        i5 = content[line+5]
        week0, increse0, quantity0 = get_data(i0)
        week1, increse1, quantity1 = get_data(i1)
        week2, increse2, quantity2 = get_data(i2)
        week3, increse3, quantity3 = get_data(i3)
        week4, increse4, quantity4 = get_data(i4)
        week5, increse5, quantity5 = get_data(i5)
        if increse0 > 0:
            result = 1
        else:
            result = 0
        # new_content = '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(increse0, week0, week1, increse1, quantity1, week2, increse2, quantity2, week3, increse3, quantity3, week4, increse4, quantity4, week5, increse5, quantity5)
        new_content = '{} 1:{} 2:{} 3:{} 4:{} 5:{} 6:{} 7:{} 8:{} 9:{} 10:{} 11:{} 12:{} 13:{} 14:{} 15:{} 16:{}\n'.format(result, week0, week1, increse1, quantity1, week2, increse2, quantity2, week3, increse3, quantity3, week4, increse4, quantity4, week5, increse5, quantity5)
        print(i0, new_content)
        new_content_list.append(new_content)
    with open(test_path, 'w') as f:
        for line in range(int(len(new_content_list) * 0.2)):
            new_content = new_content_list[line]
            f.write(new_content)
    with open(train_path, 'w') as f:
        for line in range(int(len(new_content_list) * 0.2), len(new_content_list)):
            new_content = new_content_list[line]
            f.write(new_content)


def get_data(i):
    date = i.split(',')[0]
    week = int(datetime.strptime(date, '%Y-%m-%d').weekday() + 1)
    increse = float(i.split(',')[9])
    quantity = int(i.split(',')[10])
    return week, increse, quantity



if __name__ == '__main__':
    main()