# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:29:14 2020

@author: yujin.wang
"""

import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_validate


# load or create your dataset
if __name__ == "__main__":
    target = 'FAILURE'
    features = ['TA4003','TT1081','TT990', 'HINGE WIDTH','CUSHION RADIUS','FLAPPY MASS','PLANE','NECK', 'WRAPPER']
    codes_labels = ['PLANE','NECK', 'WRAPPER']
    df_train =pd.read_csv('train_data.csv')
    df_test = pd.read_csv('test_data.csv')
    
    
    y_train = df_train['FAILURE'].values
    y_test = df_test['FAILURE'].values
    X_train = df_train[features].values
    X_test = df_test[features].values
    
    print (X_test)
    
    # create dataset for lightgbm
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
    
    params = {'num_leaves': 30, #结果对最终效果影响较大，越大值越好，太大会出现过拟合
              # 'min_data_in_leaf': 30,
              'objective': 'binary', #定义的目标函数
              'max_depth': 4,
              'learning_rate': 0.1,
               # "min_sum_hessian_in_leaf": 0.1,
              "boosting": "gbdt",
              "feature_fraction": 0.8,  #提取的特征比率
              "bagging_freq": 1,
              "bagging_fraction": 0.8,
              "bagging_seed": 11,
               "lambda_l1": 0.1,             #l1正则
              # 'lambda_l2': 0.001,     #l2正则
              "verbosity": -1,
              "nthread": 4,                #线程数量，-1表示全部线程，线程越多，运行的速度越快
              'metric': {'binary_logloss', 'auc'},  ##评价函数选择
              "random_state": 11, #随机数种子，可以防止每次运行的结果不一致
              # 'device': 'gpu' ##如果安装的事gpu版本的lightgbm,可以加快运算
              }
    
    # xgb_train = XGBClassifier_crossvalidation(xgb1,train_data,test_data, predictors,target)
    # train
    gbm = lgb.train(params,
                    lgb_train,
                    feature_name= features,
                    num_boost_round=200,
                    valid_sets=lgb_eval,
                    )
    
    print('Saving model...')
    # save model to file
    gbm.save_model('model.txt')
    
    print('Starting predicting...')
    # predict
    y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
    
    # eval
    print('The rmse of prediction is:', mean_squared_error(y_test, y_pred) ** 0.5)
    print (y_pred)
    y_pred[y_pred > 0.5] = 1
    y_pred[~(y_pred > 0.5)] = 0
    print (y_pred)
    lgb_acc =accuracy_score(y_test, y_pred)
    print ('LightGBM train model accuracy： %.3f%%' % (100*lgb_acc))