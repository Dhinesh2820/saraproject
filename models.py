from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_type = db.Column(db.Integer, index=True) 
    admin_role_type =db.Column(db.Integer)
    role_id =db.Column(db.Integer)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    mobile_number = db.Column(db.BigInteger)
    country_code =db.Column(db.String(255))
    email_id = db.Column(db.String(255))
    password =db.Column(db.String(500))
    gender =db.Column(db.SmallInteger)
    manager_name=db.Column(db.String(255))
    business_name =db.Column(db.String(255))
    city_id =db.Column(db.Integer)
    cr_number = db.Column(db.String(1000))
    status=  db.Column(db.SmallInteger, index=True) 
    reg_from =db.Column(db.SmallInteger)
    wallet = db.Column(db.Float)
    badge_count =db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    tax_certificate = db.Column(db.String(255))
    tax_certificate = db.Column(db.Text)
    logo = db.Column(db.String(255))
    



    
    
    
    
    
