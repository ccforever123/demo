import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm

def start():
    dir_path, filenames = get_file()
    for filename in filenames:
        file_path = os.path.join(dir_path, filename)
        set_data(file_path)



def get_file():
    dir_path = os.path.join(sys.path[0], 'data\data')
    for parents, dirnames, filenames in os.walk(dir_path):
        return dir_path, filenames


def open_file(dir_path, filename):
    file_path = os.path.join(dir_path, filename)
    with open(file_path, 'r') as f:
        content = f.readlines()
    return content[1:]

def set_data(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()[1:]
    filename = 1
    temp_path = os.path.join(sys.path[0], 'temp')
    while os.path.isfile(os.path.join(temp_path, '{}.csv'.format(filename))):
        filename += 1
    train_data = []
    train_target = []
    test_data = []
    test_target = []
    if len(content) > 6:
        for row in range(50, len(content)-1,-1):
            date = content[row].split(',')[0]
            print(date)
            data = [content[row].split(',')[9], content[row].split(',')[10],
                    content[row-1].split(',')[9], content[row-1].split(',')[10],
                    content[row-2].split(',')[9], content[row-2].split(',')[10],
                    content[row-3].split(',')[9], content[row-3].split(',')[10],
                    content[row-4].split(',')[9], content[row-4].split(',')[10]]
            target = content[row-5].split(',')[9]
            if target > 0:
                result = 1
            else:
                result = 0
            train_data.append(data)
            train_target.append(result)
        train_data = np.array(train_data)
        train_target = np.array(train_target)
        print(train_data)
        print(train_target)
        for row in range(6,50,-1):
            date = content[row].split(',')[0]
            print(date)
            data = [content[row].split(',')[9], content[row].split(',')[10],
                    content[row - 1].split(',')[9], content[row - 1].split(',')[10],
                    content[row - 2].split(',')[9], content[row - 2].split(',')[10],
                    content[row - 3].split(',')[9], content[row - 3].split(',')[10],
                    content[row - 4].split(',')[9], content[row - 4].split(',')[10]]
            target = content[row - 5].split(',')[9]
            train_data.append(data)
            if target > 0:
                result = 1
            else:
                result = 0
            train_target.append(result)

        test_data = np.array(test_data)
        test_target = np.array(test_target)
        print(test_data)
        print(test_target)

        clf = svm.SVC()
        clf.fit(train_data, train_target)
        result = clf.predict(test_data)
        # print(type(result))
        print(result)



if __name__ == '__main__':
    start()