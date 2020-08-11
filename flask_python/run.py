from flask import Flask, render_template, request, jsonify,send_file, make_response
from flask_cors import CORS
import os
import json
from io import BytesIO
from PIL import Image
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r".\upload"
app.config['bkg_pic'] = r".\img\background.jpg"
app.config['lb_pic'] = r".\img\Lable.png"
CORS(app)

@app.route('/')
# @app.route('/index.html')
# def index():
    # return render_template('index.html')


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

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "1.jpg")
    file_obj.save(file_path)
    
    blend_pic = editPic(app.config['bkg_pic'])
    blend_pic.pastPic(file_obj,(810,810),(132,300))
    blend_pic.pastPic(app.config['lb_pic'],(200,100),(45,254))
    print ('done')
    img_stream = base64.b64encode(blend_pic.getBytesPic)
    return img_stream 

class editPic():
    def __init__(self,pic):
        backpic = Image.open(pic)
        self.backpic = backpic.convert('RGBA') 
        
    def pastPic(self,pic,size=(100,100),pos=(100,100)):
        forepic = Image.open(pic)
        self.forpic = forepic.convert('RGBA') 
        # self.forpic.show()
        self.backpic.paste(self.forpic.resize(size),pos)
        
    @property    
    def getBytesPic(self):
        img_bytes = BytesIO()
        self.backpic.save(img_bytes, format='png')
        img_bytes = img_bytes.getvalue()
        return img_bytes

if __name__ == "__main__":
        app.run(
      host='0.0.0.0',
      port= 5000,
      debug=True
    )