from flask import jsonify
from ESRDB import db
from ESRDB import ESR
from flask import g
from ESRDB import findDB
import json
# db.create_all()
# admin = ESR(caer='yujin.wang',pe="haiming.chen",oem="GWM",esr="123456",date="2020-10-25", \
#                     proj="B01",afis="12345",cushion_type="DRR",cushion_mat="470",cover_mat="TT1081B",housing_mat="DC04", \
#                         emblem_mat = "T45M",test_res="good")

# db.session.add(admin)
# db.session.commit()
# db.session.close()
# print (ESR.query.all())
a = []
# for u in ESR.query.all():
    # u.__dict__.pop('_sa_instance_state')
    # a.append(u)
c = ESR.query.filter_by(esr= "123456").first_or_404(description='There is no data with')
print(c)
