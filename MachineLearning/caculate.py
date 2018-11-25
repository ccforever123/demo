import xgboost as xgb
import os
import numpy as np
import time
import scipy.sparse
import pickle


now = time.time()
# read in data
train_path = 'E:\\Documents\\PycharmProjects\\demo\\MachineLearning\\data\\train.txt'
test_path = 'E:\\Documents\\PycharmProjects\\demo\\MachineLearning\\data\\test.txt'

# 划分训练集与验证集
dtrain = xgb.DMatrix(train_path)
dtest = xgb.DMatrix(test_path)

# specify parameters via map, definition are same as c++ version
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic'}
# param={
# 'booster':'gbtree',
# 'objective':'binary:logistic',
# # 'num_class':10, # 类数，与 multisoftmax 并用
# 'gamma':0.1,  # 在树的叶子节点下一个分区的最小损失，越大算法模型越保守 。[0:]
# 'max_depth':10, # 构建树的深度 [1:]
# 'lambda':450,  # L2 正则项权重
# 'subsample':0.4, # 采样训练数据，设置为0.5，随机选择一般的数据实例 (0:1]
# 'colsample_bytree':0.001, # 构建树树时的采样比率 (0:1]
# #'min_child_weight':12, # 节点的最少特征数
# 'silent':1 ,
# 'eta': 0.001, # 如同学习率
# # 'seed':710,
# 'nthread':4,# cpu 线程数,根据自己U的个数适当调整
# }

# specify validations set to watch performance
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
num_round = 1000
bst = xgb.train(param, dtrain, num_round, watchlist, early_stopping_rounds=100)

# this is prediction
preds = bst.predict(dtest)
labels = dtest.get_label()
print('error=%f' % (sum(1 for i in range(len(preds)) if int(preds[i] > 0.5) != labels[i]) / float(len(preds))))
bst.save_model('0001.model')
# dump model
bst.dump_model('dump.raw.txt')
# dump model with feature map
bst.dump_model('dump.nice.txt', 'featmap.txt')

# save dmatrix into binary buffer
dtest.save_binary('dtest.buffer')
# save model
bst.save_model('xgb.model')
# load model and data in
bst2 = xgb.Booster(model_file='xgb.model')
dtest2 = xgb.DMatrix('dtest.buffer')
preds2 = bst2.predict(dtest2)
# assert they are the same
assert np.sum(np.abs(preds2 - preds)) == 0

# alternatively, you can pickle the booster
pks = pickle.dumps(bst2)
# load model and data in
bst3 = pickle.loads(pks)
preds3 = bst3.predict(dtest2)
# assert they are the same
assert np.sum(np.abs(preds3 - preds)) == 0

###
# build dmatrix from scipy.sparse
print('start running example of build DMatrix from scipy.sparse CSR Matrix')
labels = []
row = []; col = []; dat = []
i = 0
for l in open('data/train.txt'):
    arr = l.split()
    labels.append(int(arr[0]))
    for it in arr[1:]:
        k,v = it.split(':')
        row.append(i); col.append(int(k)); dat.append(float(v))
    i += 1
csr = scipy.sparse.csr_matrix((dat, (row, col)))
dtrain = xgb.DMatrix(csr, label=labels)
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
bst = xgb.train(param, dtrain, num_round, watchlist, early_stopping_rounds=100)

print('start running example of build DMatrix from scipy.sparse CSC Matrix')
# we can also construct from csc matrix
csc = scipy.sparse.csc_matrix((dat, (row, col)))
dtrain = xgb.DMatrix(csc, label=labels)
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
bst = xgb.train(param, dtrain, num_round, watchlist, early_stopping_rounds=100)

print('start running example of build DMatrix from numpy array')
# NOTE: npymat is numpy array, we will convert it into scipy.sparse.csr_matrix in internal implementation
# then convert to DMatrix
npymat = csr.todense()
dtrain = xgb.DMatrix(npymat, label=labels)
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
bst = xgb.train(param, dtrain, num_round, watchlist, early_stopping_rounds=100)