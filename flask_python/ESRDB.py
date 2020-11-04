from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB//ESR.db'

db = SQLAlchemy(app)


class ESR(db.Model):
    __tablename__ = 'ESRTable'
    id = db.Column(db.Integer, primary_key=True)
    caer = db.Column(db.String(80), nullable=False)
    pe = db.Column(db.String(80),  nullable=False)
    oem = db.Column(db.String(80),  nullable=False)
    esr = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80),  nullable=False)
    proj = db.Column(db.String(80),  nullable=False)
    afis = db.Column(db.String(80), nullable=False)
    cushion_type = db.Column(db.String(80), nullable=False)
    cushion_mat = db.Column(db.String(80), nullable=False)
    cover_mat = db.Column(db.String(80), nullable=False)
    housing_mat = db.Column(db.String(80), nullable=False)
    emblem_mat = db.Column(db.String(80), nullable=False)
    test_res = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return "{'id':'%s','caer':'%s','pe':'%s','oem':'%s','esr':'%s','date':'%s','proj':'%s','afis':'%s','cushion_type':'%s','cushion_mat':'%s','cover_mat':'%s','housing_mat':'%s','emblem_mat':'%s','test_res':'%s' }" \
            % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)
        # return "{'id':%s,'caer':%s,'pe':%s,'oem':%s,'esr':%s,'date':%s,'proj':%s,'afis':%s,'cushion_type':%s,'cushion_mat':%s}" \
        #     % (str(self.id),self.caer,self.pe,self.oem,self.esr,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat) #,self.date,self.proj,self.afis,self.cushion_type,self.cushion_mat,self.cover_mat,self.housing_mat,self.emblem_mat,self.test_res)

