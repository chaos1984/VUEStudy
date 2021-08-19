from flask import Flask, render_template, request, jsonify, send_file, make_response
from flask_cors import CORS
import pandas as pd
import numpy as np
import os
import json
import getpass
from io import BytesIO
import ESRpdf
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import base64
import pickle

import time
import hmac

from ESRDB import *
import xgboost as xgb

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['img_pic'] = r".\img\background.jpg"
app.config['ESR'] = r"../ESR"
app.config['ESRDB'] = r"../DB"
CORS(app)


@app.route('/')
# @app.route('/index.html')
def index():
    return render_template('index.html')

# @app.route('/ProjectTable')
# def writejson():
#     fout = open(r"C:\Users\yujin.wang\Desktop\Vuejs\10_MyApp\Autoliv_ESR_Foreend\public\static\data.json","r+")
#     ProjectData = json.load(fout)
#     ProjectData.append(request.args.get('ProjectTableData'))
#     json.dump(ProjectData,fout)
#     fout.close()

#     return "OK"


@app.route('/makedir', methods=['POST'])
def makedir():
    global ESRpath
    data = json.loads(request.get_data(as_text=True))
    ESRpath = app.config['ESR']+'/'+data['ESRNumber']
    try:
        os.mkdir(ESRpath)
    except:
        pass
    return (ESRpath)


@app.route('/upload', methods=["POST"])
def upload():
    # test
    # ESRpath = app.config['ESR']+"//123123"
    img_stream = ''
    file_obj = request.files['file']
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    # filename = secure_filename(file_obj.filename)

    '''
        将文件保存到本地（即当前目录）
        直接使用上传的文件对象保存
    '''

    file_path = os.path.join(ESRpath, file_obj.filename)
    file_obj.save(file_path)
    # blend_pic = blend_two_images(file_obj)

    # img_stream = base64.b64encode(blend_pic)
    print("Upload done")
    return "Upload done"


@app.route('/delete', methods=["POST"])
def delete():
    # test
    # ESRpath = app.config['ESR']+"//123123"
    img_stream = ''
    file_obj = request.get_data(as_text=True)
    print(file_obj)
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    # filename = secure_filename(file_obj.filename)

    '''
        将文件保存到本地（即当前目录）
        直接使用上传的文件对象保存
    '''

    file_path = os.path.join(ESRpath, file_obj)
    os.remove(file_path)
    # blend_pic = blend_two_images(file_obj)

    # img_stream = base64.b64encode(blend_pic)
    print("Delete done")
    return "Delete done"


@app.route('/RequestForm', methods=["POST"])
def RequestForm():
    data = json.loads(request.get_data(as_text=True))
    
    filename = data['PRJ']+'_'+data['ESR']+"_"+data['PE']+".pdf"
    a = ESRpdf.PDFGenerator(filename)
    a.genTaskPDF(data)
    return return_img_stream('.\\temp\\'+filename)

def return_img_stream(img_local_path):
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return img_stream


###############################################################DataBase ####################################################
@app.route('/getusers', methods=['GET'])
def getusers():
    if request.method == 'GET':
        a = []
        for u in User.query.all():
            try:
                u.__dict__.pop('_sa_instance_state')
                a.append(u.__dict__)
            except:
                print(u)
        return jsonify(a)


@app.route('/getdatabase', methods=['GET'])
def getdatabase():
    if request.method == 'GET':
        a = []
        for u in ESR.query.all():
            try:
                u.__dict__.pop('_sa_instance_state')
                a.append(u.__dict__)
            except:
                print(u)
        return jsonify(a)


@app.route('/findDB', methods=['POST'])
def findDB():
    obj = request.get_data(as_text=True)
    print('*****************************')
    print(obj)
    a = ESR.query.filter_by(esr=obj).count()
    print(a, type(a), a == 0)
    if a == 0:
        print('************0*************')
        return "0"  # No duplicated files
    else:
        print('************1*************')
        return "1"


@app.route('/delitem', methods=['POST'])
def delitem():
    item_id = int(request.get_data(as_text=True))
    ESR.query.filter(ESR.ID == item_id).delete()
    db.session.commit()
    db.session.close()
    return 'Delete done!'


@app.route('/dabai', methods=['POST'])
def dabai():

    data = json.loads(request.get_data(as_text=True))
    data = json.loads(data["params"]["TestData"])
    columns_name = ['PRJ ID', 'HINGE WIDTH', 'TEARLINE', 'CUSHION RADIUS',
                    'CUSHION FOLDTYPE', 'FLAPPY MASS', 'PLANE', 'NECK', 'WRAPPER']
    data = pd.DataFrame([[0, data["cover"]["hingewidth"], data["cover"]["tearline"], data["cushion"]["di"], data["cushion"]["fold"], data["cover"]
                          ["flappymass"], data["cover"]["hingeplane"], data["cover"]["hingeneck"], data["cushion"]["wrapper"]]], columns=columns_name)
    # data['COVER MAT'] = pd.Categorical(data['COVER MAT']).codes
    # data['TEARLINE'] = pd.Categorical(data['TEARLINE']).codes
    # data['WRAPPER'] = pd.Categorical(data['WRAPPER']).codes
    data["FLAPPY MASS"] = data["FLAPPY MASS"].astype('float64')
    data["HINGE WIDTH"] = data["HINGE WIDTH"].astype('float64')
    # data['NECK'] = pd.Categorical(data['NECK']).codes
    # data['PLANE'] = pd.Categorical(data['PLANE']).codes

    test_data = data[['HINGE WIDTH', 'CUSHION RADIUS',
                      'FLAPPY MASS', 'PLANE', 'NECK', 'WRAPPER']]

    # x = np.tile(test_data, (10, 1))
    y = airun(test_data)
    return str(y[0])


@app.route('/dabinfo', methods=['POST'])
def dabinfo():
    user = getpass.getuser()
    DABinfo= json.loads(request.get_data(as_text=True))
    print (DABinfo)

    copyflag = DABinfo['params']['Copy']
    print ("copyflag")
    print (copyflag)
    DABinfo = json.loads(DABinfo['params']['Dabinfo'])


    # # 添加数据到ESR DB
    # print("~~~~~~~~~~~~~~~~~~~~~")
    # # print (DABinfo["ID"])
    # print(db.session.query(func.max(ESR.ID)).scalar())
    # print("~~~~~~~~~~~~~~~~~~~~~")

    if copyflag :
        a = ESR.query.filter(ESR.PRJ == DABinfo['PRJ']).first()
        print ("a")
        print (a)
        print ( DABinfo['PRJ'])
        if a != None:
            temp = DABinfo['PRJ'].split("_V")
            version = 1+int(temp[-1])
            DABinfo['PRJ'] = temp[0] + "_V"+str(version)
        DABinfo['ID'] = db.session.query(func.max(ESR.ID)).scalar()+1
    else:
        try:
            ESR.query.filter(ESR.ID == int(DABinfo['ID'])).delete()
        except:
            DABinfo['ID'] = db.session.query(func.max(ESR.ID)).scalar()+1
            pass
    
    #AI PREDICTION
    columns_name = ['PRJ ID', 'HINGE WIDTH', 'CUSHION RADIUS', 
                     'FLAPPY MASS', 'PLANE', 'NECK', 'WRAPPER']
    data = pd.DataFrame([[0, DABinfo['H_Width'], DABinfo['C_Diam'], DABinfo['Flappy_Mass'], DABinfo['H_Plane'],DABinfo['H_Neck'],DABinfo['Wrapper']]], columns=columns_name)
    data["FLAPPY MASS"] = data["FLAPPY MASS"].astype('float64')
    data["HINGE WIDTH"] = data["HINGE WIDTH"].astype('float64')
    data['CUSHION RADIUS'] = data['CUSHION RADIUS'].astype('float64')
    # data['NECK'] = pd.Categorical(data['NECK']).codes
    # data['PLANE'] = pd.Categorical(data['PLANE']).codes

    test_data = data[['HINGE WIDTH', 'CUSHION RADIUS',
                      'FLAPPY MASS', 'PLANE', 'NECK', 'WRAPPER']]

    # x = np.tile(test_data, (10, 1))
    y = airun(test_data)
         
         
    data = ESR(
        ID=int(DABinfo['ID']),
        OEM=DABinfo['OEM'],
        PRJ=DABinfo['PRJ'],
        AFIS=DABinfo['AFIS'],
        ESR=DABinfo['ESR'],
        CAE=user,
        PE=DABinfo['PE'],
        Interface=DABinfo['Interface'],
        CV_Mat=DABinfo['CV_Mat'],
        H_Mat=DABinfo['H_Mat'],
        Tearline=DABinfo['Tearline'],
        E_Mat=DABinfo['E_Mat'],
        Inflator=DABinfo['Inflator'],
        C_Mat=DABinfo['C_Mat'],
        C_Type=DABinfo['C_Type'],
        C_Diam=DABinfo['C_Diam'],
        C_Tether=DABinfo['C_Tether'],
        C_Diffusor=DABinfo['C_Diffusor'],
        H_Width=DABinfo['H_Width'],
        Flappy_Mass=DABinfo['Flappy_Mass'],
        Wrapper=DABinfo['Wrapper'],
        Hinge_Area = DABinfo['Hinge_Area'],
        Hinge_Radius = DABinfo['Hinge_Radius'],
        H_Plane=DABinfo['H_Plane'],
        H_Neck=DABinfo['H_Neck'],
        UnderCut=DABinfo['UnderCut'],
        Simulation=str(DABinfo['Simulation']),
        Testing=str(DABinfo['Testing']),
        DateRange=str(DABinfo['DateRange']),
        CV_Height=DABinfo['CV_Height'],
        CV_Leather=DABinfo['CV_Leather'],
        Remarks = DABinfo['Remarks'],
        Log=str(DABinfo['Log']),
        AI = str(y))
    # try:
    # data = ESR( ID =int(DABinfo['ID']))
    # # ESR.query.filter(ESR.ID == int(DABinfo['ID'])).delete()
    # print (DABinfo['ID'])
    # print ('Prj is exit!')
    # except:
    # print ('New Prj')

    addESRDB(data)
    return "Done"


def addESRDB(data):

    # data = ESR(data)
    # db.create_all()
    db.session.add(data)
    db.session.commit()
    db.session.close()
    print('ok')
##############################################################################################################################
################################################################ FUNCTION ####################################################
##############################################################################################################################



def blend_two_images(img, back=app.config['img_pic']):
    img1 = Image.open(back)
    print(img1)
    img1 = img1.convert('RGBA')

    img2 = Image.open(img)
    print(img2)
    img2 = img2.convert('RGBA')
    # img2.resize((littlesize,littlesize))
    img1.paste(img2, (300, 300))
    # img1.show()
    img_bytes = BytesIO()
    img1.save(img_bytes, format='png')
    img_bytes = img_bytes.getvalue()
    return img_bytes
##############################################################################################################################
################################################################   Token  ####################################################
##############################################################################################################################
@app.route('/register', methods=['POST'])
def register():
    user = json.loads(request.get_data(as_text=True))
    print(user)
    obj = User.query.filter_by(Name=user["name"]).first()
    if not obj:
        save = User(Name=user["name"], Email=user["email"], Priority='2')
        save.hash_password(user["pass"])  # 调用密码加密方法
        db.session.add(save)
        db.session.commit()
        return 'Register success'
    else:
        return 'User name has been registered!'


@app.route('/login', methods=['POST'])
def login():
    user = json.loads(request.get_data(as_text=True))
    obj = User.query.filter_by(Name=user["name"]).first()
    if not obj:
        return res_json(201, '', '未找到该用户')
    if obj.verify_password(user["password"]):
        token = generate_token(user["name"])
        return res_json(200, token, '登录成功', obj.Priority)
    else:
        return res_json(201, '', '密码错误')

# 生成token 入参：用户id


def generate_token(key, expire=3600):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")

# 验证token 入参：用户id 和 token


def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True


def res_json(ID, data, msg, priority=2):
    res = jsonify({
        'states': ID,
        'token': data,
        'msg': msg,
        'priority': priority
    })
    return res

def airun(data):
    x = xgb.DMatrix(data)
    f = open('DABAIMODEL.dat', 'rb')
    bst = pickle.load(f)
    y = bst.predict(x)
    return (y)

if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        # host='10.123.20.248',
        port=5000,
        debug=True
    )
