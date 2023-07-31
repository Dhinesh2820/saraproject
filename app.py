from flask import Flask
from routes.admin.owner import owner_bp
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Dk282000@127.0.0.1:3306/sara'
db.init_app(app)
app.app_context().push()

migrate =Migrate(app,db)

db.create_all()

app.register_blueprint(owner_bp,url_prefix='/admin/owner')

if __name__ == '__main__':
    app.run(debug=True)