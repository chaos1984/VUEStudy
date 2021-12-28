# LIN & AI 系统开发
## 1.系统模块简介
### 1.1. 前端（\vue_foreend）
>前端采用[VUE 框架](https://vuejs.org/)进行搭建，具体搭建过程如下。
* 安装Node.js，安装成功后，`node -v`和`npm -v`测试安装成功，出现版本号即可，LIN & AI 目前基于 Node.js 是v16.13.0，npm是8.1.0。
* Vue相关组件的安装，在命令行中运行`npm install package.json`, 便会安装 LIN & AI 的依赖库。注意：Vue-cli要安装。
在当前路径启动命令行，运行`npm run serve` (需要在package.json中定义)。

### 1.2. 后端（\flask_python）
>采用Python36/Flask框架。
在当前路径启动命令行，运行`python main.py`。

**注意：** 如果直接copy 前后端文件，无需上述任何过程。
### 1.3.  数据库(flask_python\DB)
>采用SQLite轻量级数据库。
数据库文件：
    ESR.db DAB静态点爆项目数据库。
    User.db 用户数据数据库。
数据库可视化软件: [SQLiteStudio](https://sqlitestudio.pl/)。
python接口程序：ESRDB.py

### 1.4. AI模块（flask_python\DABAI）
> 采用XGBOOST对铰链过撕风险进行预测。
相关文件：
    alv_test.csv，alv_train.csv：截止到2021年8月份的所有仿真项目统计。alv_test_TT1081.csv，alv_train_TT1081.csv是从上述两个文件中提取使用TT1081材料的项目。
    DABAIMODEL.dat： 训练得到的模型。
    使用：
```python
import xgboost as xgb
import pickle
def airun(data):
    x = xgb.DMatrix(data) #输入xgboost数据
    f = open('DABAIMODEL.dat', 'rb')
    bst = pickle.load(f)
    y = bst.predict(x)
    return (y)
```

### 1.5. SMPT服务(email.py)
>E-Mail服务，目前已在服务器上调试成功。
```python
    #!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def sendEmail(sender='yujin.wang@autoliv.com',receivers=['yujin.wang@autoliv.com'],msg=[]):
    mail_host="smtp.alv.autoliv.int"  
    message = MIMEText('Python test', 'plain', 'utf-8')
    message['From'] = Header("Lin & AI", 'utf-8')
    message['To'] =  Header("", 'utf-8')
    subject = 'Python SMTP test'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("Success")
    except smtplib.SMTPException:
        print ("Error")
if __name__ == '__main__':
    sendEmail()
```
### 1.6. PDF生成程序（ESRpdf.py）
> 用于生成ESR Request.pdf 文件。


### 2 页面设计
> 两个主要的页面：ESR 项目管理界面和AI预测页面。ESR项目管理界面包括三部分：项目列表；项目图表可视化；项目进度管理。
具体内容参见PPT。



