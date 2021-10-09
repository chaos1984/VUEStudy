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
from sklearn.metrics import roc_curve, auc,recall_score,precision_score
from sklearn.preprocessing import  OneHotEncoder

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
    print ('dtrain_predprob',dtrain_predprob)
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
    fpr_train, tpr_train, _ = roc_curve(dtrain['FAILURE'].values, dtrain_predprob)
    fpr_test, tpr_test, _ = roc_curve(dtest['FAILURE'].values, dtest_predprob)
    roc_auc_train = auc(fpr_train, tpr_train)
    roc_auc_test = auc(fpr_test, tpr_test)
    plt.figure()
    lw = 2
    plt.plot(fpr_train, tpr_train, color='darkorange',
             lw=lw, label='ROC curve from train samples (area = %0.2f)' % roc_auc_train)
    plt.plot(fpr_test, tpr_test, color='blue',
             lw=lw, label='ROC curve from test samples (area = %0.2f)' % roc_auc_test)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve')
    plt.legend(loc="lower right")
    plt.show()
    return alg

def XGBtrain(alg,dtrain,param_test1,predictors,target):
    xgb_param = alg.get_xgb_params()
    dtrain = xgb.DMatrix(dtrain[predictors], label=dtrain[target])
    # watch_list = [(dtrain, 'train')]
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
    bst = xgb.train(param, dtrain, num_boost_round=alg.get_params()['n_estimators'])
    pickle.dump(bst, open("DABAIMODEL.dat", "wb")) # outpur train model
    xgb.plot_importance(bst)
    
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
    learning_rate =0.01,#和GBM中的 learning rate 参数类似。通过减少每一步的权重，可以提高模型的鲁棒性。典型值为0.01-0.2。
    n_estimators= 1000, 
    max_depth=3, #和GBM中的参数相同，这个值为树的最大深度。这个值也是用来避免过拟合的。max_depth越大，模型会学到更具体更局部的样本。需要使用CV函数来进行调优。典型值：3-1。
    min_child_weight=1, #决定最小叶子节点样本权重和。和GBM的 min_child_leaf 参数类似，但不完全一样。XGBoost的这个参数是最小样本权重的和，而GBM参数是最小样本总数。这个参数用于避免过拟合。当它的值较大时，可以避免模型学习到局部的特殊样本。但是如果这个值过高，会导致欠拟合。这个参数需要使用CV来调整
    gamma= 0.4, #在节点分裂时，只有分裂后损失函数的值下降了，才会分裂这个节点。Gamma指定了节点分裂所需的最小损失函数下降值。这个参数的值越大，算法越保守。这个参数的值和损失函数息息相关，所以是需要调整的。
    subsample=0.9, # 和GBM中的subsample参数一模一样。这个参数控制对于每棵树，随机采样的比例。减小这个参数的值，算法会更加保守，避免过拟合。但是，如果这个值设置得过小，它可能会导致欠拟合。典型值：0.5-1
    colsample_bytree=0.9,#和GBM里面的max_features参数类似。用来控制每棵随机采样的列数的占比(每一列是一个特征)。典型值：0.5-1。
    objective= 'binary:logistic',#这个参数定义需要被最小化的损失函数。最常用的值有：binary:logistic 二分类的逻辑回归，返回预测的概率(不是类别)。multi:softmax 使用softmax的多分类器，返回预测的类别(不是概率)。在这种情况下，你还需要多设一个参数：num_class(类别数目)。multi:softprob 和multi:softmax参数一样，但是返回的是每个数据属于各个类别的概率。
    nthread=4,#线程数量
    scale_pos_weight=1,#在各类别样本十分不平衡时，把这个参数设定为一个正值，可以使算法更快收敛。
    reg_alpha = 0.06,#权重的L1正则化项。(和Lasso regression类似)。可以应用在很高维度的情况下，使得算法的速度更快。
    seed=27)
    
    #用于XGBClassifier交叉验证

    xgb_train = XGBClassifier_crossvalidation(xgb1,train_data,test_data, predictors,target)
    
    #2. 用于Classfy参数调优
    #1st.选择较高的学习速率(learning rate)。一般情况下，学习速率的值为0.1。但是，对于不同的问题，理想的学习速率有时候会在0.05到0.3之间波动。选择对应于此学习速率的理想决策树数量。
    #2nd 对于给定的学习速率和决策树数量，进行决策树特定参数调优(max_depth, min_child_weight, gamma, subsample, colsample_bytree)。在确定一棵树的过程中，我们可以选择不同的参数，待会儿我会举例说明。
    #3rd xgboost的正则化参数的调优。(lambda, alpha)。这些参数可以降低模型的复杂度，从而提高模型的表现。
    #4th 降低学习速率，确定理想参数。
    param_test1 = {
            'max_depth':range(3,10,1),
            'min_child_weight':range(1,6,1),
            'gamma':[i/10.0 for i in range(0,5)],
            'subsample':[i/10.0 for i in range(6,10)],
            'colsample_bytree':[i/10.0 for i in range(6,10)],
            'reg_alpha':[i/100.0 for i in range(1,20,5)],
            # 'learning_rate':[i/100.0 for i in range(1,20,5)],
            # 'n_estimators':range(1000,20000,500)
    }
    XGBClassifier_tunrparameter(xgb1,train_data,param_test1,predictors,target)
    
    # xgb.train 进行测试预测
    
    bst = XGBtrain(xgb1,train_data,test_data, predictors,target)
    test_data1 = xgb.DMatrix(test_data[predictors])
    print (test_data[predictors])
    y_hat = bst.predict(test_data1)
    y_hat[y_hat > 0.5] = 1
    y_hat[~(y_hat > 0.5)] = 0
    xgb_acc = accuracy_score(test_data[target], y_hat)
    bst.save_model('model_file_name.json')
    bst.dump_model('dump.raw.txt')
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