from flask import Flask, render_template, request, jsonify,send_file, make_response
from flask_cors import CORS
import os
import json
import getpass
from io import BytesIO
from PIL import Image

from flask_sqlalchemy import SQLAlchemy
import base64
import ESRpdf

from ESRDB import *


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['img_pic'] = r".\img\background.jpg"
app.config['ESR'] = r"../ESR"
app.config['ESRDB'] = r"../DB"
CORS(app)

@app.route('/')
# @app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/ProjectTable')
def writejson():
    fout = open(r"C:\Users\yujin.wang\Desktop\Vuejs\10_MyApp\Autoliv_ESR_Foreend\public\static\data.json","r+")
    ProjectData = json.load(fout)
    ProjectData.append(request.args.get('ProjectTableData'))
    json.dump(ProjectData,fout)
    fout.close()
    
    return "OK"

@app.route('/makedir',methods=['POST'])
def makedir():
    global ESRpath
    data = json.loads(request.get_data(as_text=True))
    ESRpath = app.config['ESR']+'/'+data['ESRNumber']
    try:
        os.mkdir(ESRpath)
    except:
        pass
    return (ESRpath)


@app.route('/upload',methods=["POST"])
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
    print ("Upload done")
    return "Upload done"

@app.route('/delete',methods=["POST"])
def delete():
    # test
    # ESRpath = app.config['ESR']+"//123123"
    img_stream = ''
    file_obj = request.get_data(as_text=True)
    print (file_obj)
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
    print ("Delete done")
    return "Delete done"

@app.route('/RequestForm',methods=["POST"])
def RequestForm():
    data = json.loads(request.get_data(as_text=True))
    home_data = {
        "ESR": data['ESRNumber'], 
        "PE": data['PEName'], 
        "ProjectCode":data['ProjectCode'],
        "Team": data['TeamName'], 
        "Date1": data['date1'],
        "Date2": data['date2']
        }
    task_data = [("BOM",data['BOMFile'] ),("DAB CAD",data['CADFile']),("Inflator",data['InflatorFile']),("CushionFoldFile",data['CushionFoldFile']),("Cases","123")]
    filedir = ESRpath + '/'+ data['ESRNumber']+"_"+data['date1']
    a = ESRpdf.PDFGenerator(ESRpath + '/'+ data['ESRNumber']+"_"+data['date1'])
    a.genTaskPDF(home_data, task_data)
    #添加数据到ESR DB
    data = ESR(caer='yujin.wang1',pe=data['PEName'],oem="GWM",esr=data['ESRNumber'],date="2020-10-25", \
                    proj="B01",afis=data['ProjectCode'],cushion_type="DRR",cushion_mat="470",cover_mat="TT1081B",housing_mat="DC04", \
                         emblem_mat = "T45M",test_res="good")
    addESRDB(data)
    return return_img_stream(filedir+'.pdf')

# @app.route('/addESR',methods=["POST"])
# def addESR():
#     data = json.loads(request.get_data(as_text=True))
#     print (data)
#     home_data = {
#         "ESR": data['ESRNumber'], 
#         "PE": data['PEName'], 
#         "ProjectCode":data['ProjectCode'],
#         "Team": data['TeamName'], 
#         "Date1": data['date1'],
#         "Date2": data['date2']
#         }
#     admin = ESR(caer='yujin.wang',pe="haiming.chen",oem="GWM",esr="123456",date="2020-10-25", \
#                         proj="B01",afis="12345",cushion_type="DRR",cushion_mat="470",cover_mat="TT1081B",housing_mat="DC04", \
#                             emblem_mat = "T45M",test_res="good")
#     db.session.add(admin)
#     db.session.commit()
#     db.session.close()   

###############################################################DataBase #################################################### 
@app.route('/getdatabase', methods = ['GET'])
def getdatabase():
    if request.method == 'GET':
        a = []
        for u in ESR.query.all():
            u.__dict__.pop('_sa_instance_state')
            a.append(u.__dict__)
       
        return jsonify(a)
        
@app.route('/findDB', methods = ['POST'])
def findDB():
    obj = request.get_data(as_text=True)
    print ('*****************************')
    print (obj)
    a  = ESR.query.filter_by(esr= obj).count()
    print (a,type(a),a==0)
    if a == 0:
        print ('************0*************')
        return "0" #No duplicated files
    else :
        print ('************1*************')
        return "1"
@app.route('/delitem', methods = ['POST'])
def delitem():
     item_id = request.get_data(as_text=True)
     print (item_id)
     db.session.query(ESR).filter(ESR.id==item_id).delete()
     db.session.commit()
     db.session.close()
     return 'Delete done!'
    
##############################################################################################################################
################################################################ FUNCTION ####################################################
##############################################################################################################################
def addESRDB(data):
    db.create_all()
    db.session.add(data)
    db.session.commit()
    db.session.close()
    print ('ok')
    
def return_img_stream(img_local_path):
  img_stream = ''
  with open(img_local_path, 'rb') as img_f:
    img_stream = img_f.read()
    img_stream = base64.b64encode(img_stream)
  return img_stream 
 
def blend_two_images(img,back=app.config['img_pic']):
    img1 = Image.open(back)
    print(img1)
    img1 = img1.convert('RGBA')
 
    img2 = Image.open(img)
    print(img2)
    img2 = img2.convert('RGBA')
    # img2.resize((littlesize,littlesize))
    img1.paste(img2,(300,300))
    # img1.show()
    img_bytes = BytesIO()
    img1.save(img_bytes, format='png')
    img_bytes = img_bytes.getvalue()
    return img_bytes
    

if __name__ == "__main__":
    app.run(
      host='127.0.0.1',
      # host='10.123.20.248',
      port= 5000,
      debug=True
    )