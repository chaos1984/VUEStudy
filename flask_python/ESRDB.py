from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB//ESR.db'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True


db = SQLAlchemy(app)


class ESR(db.Model):
    __tablename__ = 'ESRTable'
    OEM = db.Column(db.String(80),nullable=False)
    ID = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    # ID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"), primary_key=True)
    PRJ = db.Column(db.String(80), nullable=False)
    AFIS = db.Column(db.String(80), nullable=False)
    ESR = db.Column(db.String(80), nullable=False)
    PE = db.Column(db.String(80),  nullable=False)
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
    Flappy_Mass = db.Column(db.Float(), nullable=False)
    Wrapper = db.Column(db.String(80), nullable=False)
    H_Plane = db.Column(db.String(80), nullable=False)
    H_Neck = db.Column(db.String(80), nullable=False)
    Daokou = db.Column(db.String(80), nullable=False)
    Simulation = db.Column(db.String(80), nullable=False)
    Testing = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "{'id':'%s','caer':'%s','pe':'%s','oem':'%s','esr':'%s','date':'%s','proj':'%s','afis':'%s','cushion_type':'%s','cushion_mat':'%s','cover_mat':'%s','housing_mat':'%s','emblem_mat':'%s','test_res':'%s' }" \
            % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)
        # return "{'id':%s,'caer':%s,'pe':%s,'oem':%s,'esr':%s,'date':%s,'proj':%s,'afis':%s,'cushion_type':%s,'cushion_mat':%s}" \
        #     % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat) #,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)

