from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB//ESR.db'

db = SQLAlchemy(app)


class ESR(db.Model):
    __tablename__ = 'ESRTable'
    ID = db.Column(db.Integer, primary_key=True)
    PRJ = db.Column(db.String(80), nullable=False)
    PE = db.Column(db.String(80),  nullable=False)
    Interface = db.Column(db.String(80),  nullable=False)
    ESR = db.Column(db.String(80), nullable=False)
    CV_Mat = db.Column(db.String(80),  nullable=False)
    H_Mat = db.Column(db.String(80), nullable=False)
    E_Mat = db.Column(db.String(80), nullable=False)
    Tearline = db.Column(db.String(80), nullable=False)
    C_Tether = db.Column(db.String(80), nullable=False)
    C_Mat = db.Column(db.String(80), nullable=False)
    C_Type = db.Column(db.String(80), nullable=False)
    C_Diam = db.Column(db.String(80), nullable=False)
    Wrapper = db.Column(db.String(80), nullable=False)
    Flappy_Mass = db.Column(db.Float(), nullable=False)
    H_Width = db.Column(db.Float(), nullable=False)
    H_Plane = db.Column(db.String(80), nullable=False)
    H_Neck = db.Column(db.String(80), nullable=False)
    Inflator = db.Column(db.String(80), nullable=False)
    Failure = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "{'id':'%s','caer':'%s','pe':'%s','oem':'%s','esr':'%s','date':'%s','proj':'%s','afis':'%s','cushion_type':'%s','cushion_mat':'%s','cover_mat':'%s','housing_mat':'%s','emblem_mat':'%s','test_res':'%s' }" \
            % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)
        # return "{'id':%s,'caer':%s,'pe':%s,'oem':%s,'esr':%s,'date':%s,'proj':%s,'afis':%s,'cushion_type':%s,'cushion_mat':%s}" \
        #     % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat) #,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)

