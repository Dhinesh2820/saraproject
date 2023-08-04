from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary
from flask_migrate import Migrate
from datetime import datetime
from models import db
from models.category import Category
from sqlalchemy.orm import relationship
from alembic import op


class Store_timings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    day = db.Column(db.SmallInteger)
    open_time = db.Column(db.Time)
    close_time = db.Column(db.Time)
    available = db.Column(db.SmallInteger)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    fk_store_timings = relationship('Users', backref='Store_timings')

class Store_staff_timings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    
class Store_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer)
    category_id= db.Column(db.Integer,db.ForeignKey('category.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    fk_store_category = relationship('Category', backref='Store_category')
    
    
class Store_main_service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer)
    title = db.Column(db.String(250))
    ar_title =db.Column(db.String(250))
    position = db.Column(db.Integer)
    status=  db.Column(db.SmallInteger, index=True) 
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    
    
class Store_service(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        store_id = db.Column(db.Integer)
        main_service_id = db.Column(db.Integer)
        parent_id = db.Column(db.Integer)
        title = db.Column(db.String(250))
        ar_title =db.Column(db.String(250))
        description = db.Column(db.Text)
        ar_description = db.Column(db.Text)
        timing = db.Column(db.Time)
        level = db.Column(db.SmallInteger)
        price = db.Column(db.Float)
        created_on = db.Column(db.DateTime, default=datetime.utcnow)
        updated_on = db.Column(db.DateTime, default=datetime.utcnow)
        created_by = db.Column(db.Integer)
        updated_by = db.Column(db.Integer)
        
        
class Store_staff(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        store_id = db.Column(db.Integer)
        name = db.Column(db.String(255))
        contact_no = db.Column(db.String(50))
        email_id = db.Column(db.String(255))
        created_on = db.Column(db.DateTime, default=datetime.utcnow)
        updated_on = db.Column(db.DateTime, default=datetime.utcnow)
        created_by = db.Column(db.Integer)
        updated_by = db.Column(db.Integer)
        
        
class Store_staff_service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer)
    staff_id = db.Column(db.Integer)
    service_id = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    
    
class Store_cancellation(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        store_id = db.Column(db.Integer)
        before_time = db.Column(db.Time)
        price = db.Column(db.Float)
        status=  db.Column(db.SmallInteger, index=True) 
        created_on = db.Column(db.DateTime, default=datetime.utcnow)
        updated_on = db.Column(db.DateTime, default=datetime.utcnow)
        created_by = db.Column(db.Integer)
        updated_by = db.Column(db.Integer)