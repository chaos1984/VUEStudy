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

def trainmodel(alg,dtrain,param_test1,predictors,target):

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
        seed=xgb_param["scale_pos_weight"]), 
    param_grid = param_test1,
    scoring='roc_auc',
    n_jobs=4,
    iid=False,
    cv=5)
    gsearch1.fit(dtrain[predictors],dtrain[target])
    print (gsearch1.best_estimator_)
    print (gsearch1.best_params_, gsearch1.best_score_)
    
    
def modelfit(alg, dtrain,dtest,predictors,target,useTrainCV=True, cv_folds=3, early_stopping_rounds=1000):

    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(np.tile(dtrain[predictors].values,(5,1)), label=np.tile(dtrain[target].values,(5,)),silent=True)
        # xgtrain = xgb.DMatrix(dtrain[predictors].values, label=dtrain[target].values)
        # print ("alg.get_params()['n_estimators']\n",alg.get_params()['n_estimators'])
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
            metrics='auc', early_stopping_rounds=early_stopping_rounds,verbose_eval=False)
        # print ("cvresult\n",cvresult)

        alg.set_params(n_estimators=cvresult.shape[0])

    # print ("dtrain[predictors]\n",dtrain[predictors])
    # print (" dtrain['FAILURE']\n", dtrain['FAILURE'])
    #Fit the algorithm on the data
    alg.fit(dtrain[predictors], dtrain['FAILURE'],eval_metric='auc')
    alg.fit(dtest[predictors], dtest['FAILURE'],eval_metric='auc')
        
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
    
    # xgb.plot_importance(alg,max_num_features =10)
                    
    feat_imp = pd.Series(alg.get_booster().get_fscore()).sort_values(ascending=False)
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')

    return alg

def loaddata(file,codes_labels):
    data = pd.read_csv(file)
    for item in codes_labels:
        data[item] = pd.Categorical(data[item]).codes
    return data


if __name__ == "__main__":
    feature_labels =['PRJ. ID','COVER MAT', 'HINGE WIDTH','CUSHION RADIUS','FLAPPY MASS','PLANE','NECK', 'WRAPPER','FAILURE']
    codes_labels = ['COVER MAT', 'PLANE','NECK', 'WRAPPER']
    train_data = loaddata('alv_train.csv',codes_labels)
    test_data = loaddata('alv_test.csv',codes_labels)
    train_data = train_data[feature_labels]
    test_data = test_data[feature_labels]
    target = 'FAILURE'
    IDcol = 'PRJ. ID'
    
    predictors = [x for x in train_data.columns if x not in [target, IDcol]]
    # print ("predictors\n",predictors)
    # print ("train\n",train[predictors].values)
    # XGBoost
    xgb1 = XGBClassifier(
    learning_rate =0.1,
    n_estimators= 1000,
    max_depth=3,
    min_child_weight=1,
    gamma=0,
    subsample=0.8,
    colsample_bytree=0.8,
    objective= 'binary:logistic',
    nthread=4,
    scale_pos_weight=1,
    seed=27)


    param_test1 = {
     'max_depth':range(3,10,2),
     'min_child_weight':range(1,6,2)
    }
    
    trainmodel(xgb1,train_data,param_test1,predictors,target)
    
    # xgb_train = modelfit(xgb1,train_data,test_data, predictors,target)
    # results = cross_val_score(nst, X, Y, cv=kfold)
    # print("Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
    
    
