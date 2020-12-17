# /usr/bin/python
# -*- encoding:utf-8 -*-

import xgboost as xgb
from xgboost.sklearn import XGBClassifier
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_validate


import pandas as pd
import csv
import pydotplus
from sklearn import tree
import pickle

plt.rcParams['figure.figsize'] = (16.0, 8.0) 



def load_data(file_name, is_train):
    data = pd.read_csv(file_name)  # 数据文件路径
    pd.set_option('display.width', 200)
    print ('data.describe() = \n', data.describe())

    #
    data['COVER MAT'] = pd.Categorical(data['COVER MAT']).codes
    data['HOUSING MAT'] = pd.Categorical(data['HOUSING MAT']).codes
    data['TEARLINE'] = pd.Categorical(data['TEARLINE']).codes
    data['INTERFACE'] = pd.Categorical(data['INTERFACE']).codes
    # data['FLAPPY SHAPE'] = pd.Categorical(data['FLAPPY SHAPE']).codes
    # data['CUSHION RADIUS'] = pd.Categorical(data['CUSHION RADIUS']).codes
    data['WRAPPER'] = pd.Categorical(data['WRAPPER']).codes
    data['CUSHION FOLDTYPE'] = pd.Categorical(data['CUSHION FOLDTYPE']).codes
    data['INFLATOR'] = pd.Categorical(data['INFLATOR']).codes

    print (data.describe())
    data.to_csv('New_Data.csv')
    # x = data[['COVER MAT', 'HOUSING MAT', 'TEARLINE', 'INTERFACE', 'FLAPPY SHAPE', 'CUSHION RADIUS', 'WRAPPER','CUSHION FOLDTYPE']]
    x = data[['COVER MAT', 'HINGE WIDTH','CUSHION RADIUS','FLAPPY MASS','PLANE','NECK', 'WRAPPER']]
    if is_train == False:
        print ('~~~~~~~~~~~~~~~~~~~~')
        print (x)
    y = None
    if 'FAILURE' in data:
        y = data['FAILURE']

    x = np.array(x)
    y = np.array(y)

    # 思考：这样做，其实发生了什么？
    x = np.tile(x, (10, 1))
    # print ('x',x)
    y = np.tile(y, (10, ))
    if is_train:
        return x, y

    return x, data['PRJ. ID']


def write_result(c):
    file_name = 'alv_test.csv'
    
    data = pd.read_csv(file_name)
    test_num = len(data['FAILURE'])
    x, prj_id = load_data(file_name, False)
    x = xgb.DMatrix(x)
    y = c.predict(x)
    print ("#######################")
    print (y[:test_num])
    y[y > 0.5] = 1
    y[~(y > 0.5)] = 0

    xgbtestacc = accuracy_score(data['FAILURE'], y[:test_num])
    for num in range(test_num):
        if y[num] != data['FAILURE'][num]:
            print ("ERROR:",data["PRJ."][num])
    print ('XGBoost test model accuracy：%.3f%%' % (100*xgbtestacc))


if __name__ == "__main__":
    x, y = load_data('alv_train.csv', True)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)
    
    # XGBoost
    data_train = xgb.DMatrix(x_train, label=y_train)
    data_test = xgb.DMatrix(x_test, label=y_test)
    watch_list = [(data_test, 'eval'), (data_train, 'train')]
    param = {'max_depth': 6, 'eta': 0.8, 'silent': 1, 'objective': 'binary:logistic'}
             # 'subsample': 1, 'alpha': 0, 'lambda': 0, 'min_child_weight': 1}

    bst = xgb.train(param, data_train, num_boost_round=20, evals=watch_list)
   
    
    # cv_score = cross_validation.cross_val_score(alg, dtrain[predictors], dtrain['Disbursed'], cv=cv_folds, scoring='roc_auc')
    
    
    y_hat = bst.predict(data_test)
    
    y_hat[y_hat > 0.5] = 1
    y_hat[~(y_hat > 0.5)] = 0
    xgb_acc = accuracy_score(y_test, y_hat)
    bst.save_model('model_file_name.json')
    bst.dump_model('dump.raw.txt')
    xgb.plot_importance(bst)
    pickle.dump(bst, open("DABAIMODEL.dat", "wb")) # outpur train model
    f=open('DABAIMODEL.dat','rb')
    bst1 = pickle.load(f) #载入模型
    y_hat_1 = bst1.predict(data_test)
    y_hat_1[y_hat_1 > 0.5] = 1
    y_hat_1[~(y_hat_1 > 0.5)] = 0
    xgb_acc_1 = accuracy_score(y_test, y_hat_1)
    
    write_result(bst) # wrie test result
    # xgb.plot_tree(bst, num_trees=2)
    print ('XGBoost train model accuracy：%.3f%%' % (100*xgb_acc))
