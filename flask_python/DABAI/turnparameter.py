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
from sklearn import metrics
from sklearn.model_selection import GridSearchCV   #Perforing grid search


import pandas as pd
import csv
import pydotplus
from sklearn import tree
import pickle

plt.rcParams['figure.figsize'] = (16.0, 8.0) 

def XGBClassifier_tunrparameter(alg,dtrain,param_test1,predictors,target):

    xgb_param = alg.get_xgb_params()
    gsearch1 = GridSearchCV(estimator =XGBClassifier(
        learning_rate =xgb_param["learning_rate"],
        n_estimators=alg.get_params()['n_estimators'],
        max_depth=xgb_param["max_depth"],
        min_child_weight=xgb_param["min_child_weight"],
        gamma=xgb_param["gamma"],
        subsample=xgb_param["subsample"],
        colsample_bytree=xgb_param["colsample_bytree"],
        objective= xgb_param["objective"],
        nthread=xgb_param["nthread"],
        scale_pos_weight=xgb_param["scale_pos_weight"],
        seed=xgb_param["scale_pos_weight"], 
        reg_alpha=xgb_param["scale_pos_weight"]),
    param_grid = param_test1,
    scoring='roc_auc',
    n_jobs=4,
    iid=False,
    cv=5)
    gsearch1.fit(dtrain[predictors],dtrain[target])
    print (gsearch1.best_estimator_)
    print (gsearch1.best_params_, gsearch1.best_score_)
    
    
def XGBClassifier_crossvalidation(alg, dtrain,dtest,predictors,target,useTrainCV=True, cv_folds=3, early_stopping_rounds=1000):

    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(np.tile(dtrain[predictors].values,(5,1)), label=np.tile(dtrain[target].values,(5,)),silent=True)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
            metrics='auc', early_stopping_rounds=early_stopping_rounds,verbose_eval=True)

        alg.set_params(n_estimators=cvresult.shape[0])
    #Fit the algorithm on the data
    alg.fit(dtrain[predictors], dtrain['FAILURE'],eval_metric='auc')

        
    #Predict training set:

    dtrain_predictions = alg.predict(dtrain[predictors])
    dtrain_predprob = alg.predict_proba(dtrain[predictors])[:,1]
    
    dtest_predictions = alg.predict(dtest[predictors])
    dtest_predprob = alg.predict_proba(dtest[predictors])[:,1]
        
    #Print model report:
    print ("\nModel Report")
    print ("Accuracy : %.4g" % metrics.accuracy_score(dtrain['FAILURE'].values, dtrain_predictions))
    print ("AUC Score (Train): %f" % metrics.roc_auc_score(dtrain['FAILURE'], dtrain_predprob))
    print ("Accuracy : %.4g" % metrics.accuracy_score(dtest['FAILURE'].values, dtest_predictions))
    print ("AUC Score (test): %f" % metrics.roc_auc_score(dtest['FAILURE'], dtest_predprob))
    
    # xgb.plot_importance(alg,max_num_features =10,importance_type="gain")
                    
    feat_imp = pd.Series(alg.get_booster().get_score(importance_type='weight')).sort_values(ascending=False)
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')

    return alg

def XGBtrain(alg,dtrain,param_test1,predictors,target):
    xgb_param = alg.get_xgb_params()
    dtrain = xgb.DMatrix(dtrain[predictors], label=dtrain[target])
    watch_list = [(dtrain, 'train')]
    param = {'max_depth': xgb_param["max_depth"],
             "min_child_weight":xgb_param["min_child_weight"],
             'eta':xgb_param["learning_rate"], 
             'alpha':xgb_param["reg_alpha"],
             'silent': 2, 
             'objective': 'binary:logistic',
             'gamma': xgb_param["gamma"],
             'subsample':xgb_param["subsample"],
             'colsample_bytree':xgb_param["colsample_bytree"],
             'nthred':4,
             'scale_pos_weight':xgb_param["scale_pos_weight"] }
    bst = xgb.train(param, dtrain, num_boost_round=alg.get_params()['n_estimators'],evals = watch_list)
    pickle.dump(bst, open("DABAIMODEL.dat", "wb")) # outpur train model
    # xgb.plot_importance(bst)
    
    return bst

def loadtrainmodel(modelfile):
    f = open(modelfile,'rb')
    return pickle.load(f)
    

def loaddata(file,codes_labels):
    data = pd.read_csv(file)
    for item in codes_labels:
        data[item] = pd.Categorical(data[item]).codes
    return data


if __name__ == "__main__":
    feature_labels =['PRJ. ID','COVER MAT', 'HINGE WIDTH','CUSHION RADIUS','FLAPPY MASS','PLANE','NECK', 'WRAPPER','FAILURE']
    codes_labels = ['COVER MAT','PLANE','NECK', 'WRAPPER']
    train_data = loaddata('alv_train.csv',codes_labels)
    test_data = loaddata('alv_test.csv',codes_labels)
    train_data = train_data[feature_labels]
    test_data = test_data[feature_labels]
    target = 'FAILURE'
    IDcol = 'PRJ. ID'
    
    predictors = [x for x in train_data.columns if x not in [target, IDcol]]
    # print ("train\n",train[predictors].values)
    # 1. XGBoost
    xgb1 = XGBClassifier(
    learning_rate =0.01,
    n_estimators= 5000,
    max_depth=2,
    min_child_weight=1,
    gamma= 0.08,
    subsample=0.61,
    colsample_bytree=0.58,
    objective= 'binary:logistic',
    nthread=4,
    scale_pos_weight=1,
    reg_alpha = 0.625,
    seed=27)
    
    #用于XGBClassifier交叉验证
    # xgb_train = XGBClassifier_crossvalidation(xgb1,train_data,test_data, predictors,target)
    
    #2. 用于Classfy参数调优
    # param_test1 = {
    #     'reg_alpha':[0.6,0.625,0.65]
    # }
    # XGBClassifier_tunrparameter(xgb1,train_data,param_test1,predictors,target)
    
    # xgb.train 进行测试预测
    bst = XGBtrain(xgb1,train_data,test_data, predictors,target)
    test_data1 = xgb.DMatrix(test_data[predictors])
    print (test_data[predictors])
    y_hat = bst.predict(test_data1)
    y_hat[y_hat > 0.3] = 1
    y_hat[~(y_hat > 0.3)] = 0
    xgb_acc = accuracy_score(test_data[target], y_hat)
    # bst.save_model('model_file_name.json')
    # bst.dump_model('dump.raw.txt')
    pickle.dump(bst, open("DABAIMODEL.dat", "wb"))
    test_num = len(test_data[target])
    for num in range(test_num):
        if y_hat[num] != test_data[target][num]:
            print ("ERROR:",test_data["PRJ. ID"][num],'Score:',y_hat[num] )
    print ('XGBoost train model accuracy： %.3f%%' % (100*xgb_acc))
    
    #load train model
    bst1 = loadtrainmodel("DABAIMODEL.dat")
    y_hat = bst1.predict(test_data1)
    print (y_hat)