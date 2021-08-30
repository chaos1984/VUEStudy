from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context

app = Flask(__name__)

SQLALCHEMY_BINDS = {
    'ESRs': 'sqlite:///DB//ESR.db',
    'Users': 'sqlite:///DB//User.db'
}


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB//ESR.db'
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False


db = SQLAlchemy(app)


class ESR(db.Model):
    __bind_key__ = 'ESRs' # 已设置__bind_key__,则采用设置的数据库引擎
    __tablename__ = 'ESRTable'
    
    ID = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    
    OEM = db.Column(db.String(80),nullable=False)
    
    PRJ = db.Column(db.String(80), nullable=False)
    AFIS = db.Column(db.String(80), nullable=False)
    ESR = db.Column(db.String(80), nullable=False)
    PE = db.Column(db.String(80),  nullable=False)
    CAE = db.Column(db.String(80),  nullable=False)
    Interface = db.Column(db.String(80),  nullable=False)
    CV_Mat = db.Column(db.String(80),  nullable=False)
    H_Mat = db.Column(db.String(80), nullable=False)
    Tearline = db.Column(db.String(80), nullable=False)
    E_Mat = db.Column(db.String(80), nullable=False)
    Inflator = db.Column(db.String(80), nullable=False)
    C_Mat = db.Column(db.String(80), nullable=False)
    C_Type = db.Column(db.String(80), nullable=False)
    C_Diam = db.Column(db.String(80), nullable=False)
    C_Tether = db.Column(db.String(80), nullable=False)
    H_Width = db.Column(db.Float(), nullable=False)
    C_Diffusor = db.Column(db.String(80), nullable=False)
    Flappy_Mass = db.Column(db.Float(), nullable=False)
    Hinge_Area= db.Column(db.Float(), nullable=False)
    Hinge_Width= db.Column(db.Float(), nullable=False)
    Hinge_Radius= db.Column(db.Float(), nullable=False)
    Wrapper = db.Column(db.Boolean, nullable=False)
    H_Plane = db.Column(db.Boolean, nullable=False)
    H_Neck = db.Column(db.Boolean, nullable=False)
    UnderCut = db.Column(db.Boolean, nullable=False)
    Simulation = db.Column(db.String(80), nullable=False)
    Testing = db.Column(db.String(80), nullable=False)
    DateRange = db.Column(db.String(80), nullable=False)
    CV_Height = db.Column(db.Float(), nullable=False)
    CV_Leather = db.Column(db.Boolean, nullable=False)
    PPT = db.Column(db.String(800), nullable=False)
    Remarks = db.Column(db.String(800), nullable=False)
    Log = db.Column(db.String(80), nullable=False)
    AI = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "{'ID':'%s','OEM':'%s','PRJ':'%s' ,'AFIS':'%s','ESR':'%s','PE':'%s','CAE':'%s','Interface':'%s','CV_Mat':'%s','H_Mat':'%s','Tearline':'%s','E_Mat':'%s','Inflator':'%s','C_Mat':'%s','C_Type':'%s','C_Diam':'%s','C_Tether':'%s','H_Width':'%s','Flappy_Mass':'%s','Wrapper':'%s','Hinge_Area':'%s','Hinge_Width':'%s','Hinge_Radius':'%s','H_Plane':'%s','H_Neck':'%s','UnderCut':'%s','Simulation':'%s','Testing':'%s','DateRange':'%s','CV_Height':'%s','CV_Leather':'%s','PPT':'%s','Remarks':'%s','Log':'%s','AI':'%s'}" \
            % (str(self.ID),self.OEM,self.PRJ,self.AFIS,self.ESR,self.PE,self.CAE,self.Interface,self.CV_Mat,self.H_Mat,self.Tearline,self.E_Mat,self.Inflator,self.C_Mat,self.C_Type,self.C_Diam,self.C_Tether,self.H_Width,self.Flappy_Mass,self.Wrapper,self.Hinge_Area,self.Hinge_Width,self.Hinge_Radius,self.H_Plane,self.H_Neck,self.UnderCut,self.Simulation,self.Testing,self.DateRange,self.CV_Height,self.CV_Leather,self.PPT,self.Remarks,self.Log,self.AI)
  
        # return "{'id':%s,'caer':%s,'pe':%s,'oem':%s,'esr':%s,'date':%s,'proj':%s,'afis':%s,'cushion_type':%s,'cushion_mat':%s}" \
        #     % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat) #,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)

class User(db.Model):
    __bind_key__ = 'Users' # 已设置__bind_key__,则采用设置的数据库引擎
    __tablename__ = 'User'
    ID = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    
    Name = db.Column(db.String(80),nullable=False)
    Password = db.Column(db.Text,nullable=False)
    Email = db.Column(db.String(80),nullable=False)
    Priority = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return "{'ID':'%s','Name':'%s','Password':'%s' ,'Email':'%s','Priority':'%s'}" \
            % (str(self.ID),self.Name,self.Password,self.Email,self.Priority)
    def hash_password(self,password): #给密码加密方法
        self.Password = pwd_context.encrypt(password)
 
    def verify_password(self,password): #验证密码方法
        print (password,self.Password)
        return pwd_context.verify(password, self.Password)

# db.create_all() # 未指定bind,则使用默认的数据库引擎
db.create_all(bind='Users') # 指定bind,则使用指定的数据库引擎
db.create_all(bind='ESRs')
