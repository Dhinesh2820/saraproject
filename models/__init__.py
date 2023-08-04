from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db = SQLAlchemy()

SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:8mGphy8bssn8dKrQ0mNG@pythonrds.ctrd2wzuglzf.ap-south-1.rds.amazonaws.com:3306/local'


engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session() 