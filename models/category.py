from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary
from flask_migrate import Migrate
from datetime import datetime
from models import db
from sqlalchemy.orm import relationship
from alembic import op




class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    ar_title =db.Column(db.String(250))
    image = db.Column(db.Text)
    status=db.Column(db.SmallInteger, index=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    # fk_category = relationship('Store_category', back_populates='fk_store_category')
    