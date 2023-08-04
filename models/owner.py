from datetime import datetime
from models import db



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_type = db.Column(db.Integer, index=True) 
    admin_role_type =db.Column(db.Integer)
    parent_id = db.Column(db.Integer)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    mobile_number = db.Column(db.BigInteger)
    country_code =db.Column(db.String(255))
    email_id = db.Column(db.String(255))
    password =db.Column(db.String(500))
    gender =db.Column(db.SmallInteger)
    manager_name=db.Column(db.String(255))
    business_name =db.Column(db.String(255))
    cr_number = db.Column(db.String(1000))
    status=  db.Column(db.SmallInteger, index=True) 
    wallet = db.Column(db.Float)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    tax_certificate = db.Column(db.String(255))
    logo = db.Column(db.String(255))
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    area = db.Column(db.Integer)
    address = db.Column(db.String(255))
    about = db.Column(db.String(255))
 
    

    
    
    
    
    
