from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB//ESR.db'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = False


db = SQLAlchemy(app)


class ESR(db.Model):
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
    Wrapper = db.Column(db.Boolean, nullable=False)
    H_Plane = db.Column(db.Boolean, nullable=False)
    H_Neck = db.Column(db.Boolean, nullable=False)
    Daokou = db.Column(db.Boolean, nullable=False)
    Simulation = db.Column(db.String(80), nullable=False)
    Testing = db.Column(db.String(80), nullable=False)
    DateRange = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "{'ID':'%s','OEM':'%s','PRJ':'%s' ,'AFIS':'%s','ESR':'%s','PE':'%s','CAE':'%s','Interface':'%s','CV_Mat':'%s','H_Mat':'%s','Tearline':'%s','E_Mat':'%s','Inflator':'%s','C_Mat':'%s','C_Type':'%s','C_Diam':'%s','C_Tether':'%s','H_Width':'%s','Flappy_Mass':'%s','Wrapper':'%s','H_Plane':'%s','H_Neck':'%s','Daokou':'%s','Simulation':'%s','Testing':'%s','DateRange':'%s')}" \
            % (str(self.ID),self.OEM,self.PRJ,self.AFIS,self.ESR,self.PE,self.CAE,self.Interface,self.CV_Mat,self.H_Mat,self.Tearline,self.E_Mat,self.Inflator,self.C_Mat,self.C_Type,self.C_Diam,self.C_Tether,self.H_Width,self.Flappy_Mass,self.Wrapper,self.H_Plane,self.H_Neck,self.Daokou,self.Simulation,self.Testing,self.DateRange)
  
        # return "{'id':%s,'caer':%s,'pe':%s,'oem':%s,'esr':%s,'date':%s,'proj':%s,'afis':%s,'cushion_type':%s,'cushion_mat':%s}" \
        #     % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat) #,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)

