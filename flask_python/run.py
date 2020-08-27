from flask import Flask, render_template, request, jsonify,send_file, make_response
from flask_cors import CORS
import os
import json
from io import BytesIO
from PIL import Image
import base64
import ESRpdf


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r".\upload"
app.config['img_pic'] = r".\img\background.jpg"
CORS(app)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('//dist//index.html')


@app.route('/addnumber')
def add():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return jsonify(result=a + b)
    
@app.route('/ProjectTable')
def writejson():
    fout = open(r"C:\Users\yujin.wang\Desktop\Vuejs\10_MyApp\vuetify-app\public\static\data.json",'w')
    ProjectData = request.args.get('ProjectTableData')
    # print (json.load(ProjectData))
    json.dump(ProjectData,fout)
    return "OK"

@app.route('/upload',methods=["POST"])
def upload():
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

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_obj.filename)
    file_obj.save(file_path)
    # blend_pic = blend_two_images(file_obj)

    # img_stream = base64.b64encode(blend_pic)
    print ("Upload done")
    return "Upload done"

@app.route('/RequestForm',methods=["POST"])
def RequestForm():  
    data = json.loads(request.get_data(as_text=True))
    print (data)
    home_data = {
        "ESR": data['ESRNumber'], 
        "PE": data['PEName'], 
        "ProjectCode":data['ProjectCode'],
        "Team": data['TeamName'], 
        "Date1": data['date1'],
        "Date2": data['date2']
        }
        
    task_data = [("BOM",data['BOMFile'] ),("DAB CAD",data['CADFile']),("Inflator",data['InflatorFile']),("CushionFoldFile",data['CushionFoldFile']),("Cases","123")]
    a = ESRpdf.PDFGenerator(data['ESRNumber']+"_"+data['date1'])
    
    a.genTaskPDF(home_data, task_data)
    return "OK"
    
    
def return_img_stream(img_local_path):
  img_stream = ''
  with open(img_local_path, 'rb') as img_f:
    print ('ok')
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
      port= 5000,
      debug=True
    )