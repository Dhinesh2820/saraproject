# from flask import Flask
# from routes.admin.owner import owner_bp
# from routes.admin.category import category_bp
# from routes.admin.city import city_bp
# from models import db
# from models.category import Category
# from models.store import Store_timings
from models.store import Store_category
# from models.store import Store_main_service
# from models.store import Store_service
# from models.store import Store_staff
# from models.store import Store_staff_service
# from models.store import Store_cancellation
# from models.store import Store_staff_timings
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://bloosrootuser:ZqKmfJqUgenk3yOtW12hJ3@bloss-staging.crxhffngcxjs.ap-south-1.rds.amazonaws.com:3306/local'
# db.init_app(app)
# app.app_context().push()

# migrate =Migrate(app,db)

# db.create_all()

# app.register_blueprint(owner_bp,url_prefix='/admin/owner')
# app.register_blueprint(category_bp,url_prefix='/admin/category')
# app.register_blueprint(city_bp,url_prefix='/admin/city')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from routes.admin.owner import owner_bp
from routes.admin.category import category_bp
from routes.admin.city import city_bp
from models import db
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('models/__init__.py')
db.init_app(app)
jwt = JWTManager(app)


# db.create_all()
migrate =Migrate(app,db)

app.register_blueprint(owner_bp,url_prefix='/admin/owner')
app.register_blueprint(category_bp,url_prefix='/admin/category')
app.register_blueprint(city_bp,url_prefix='/admin/city')

if __name__ == '__main__':
    app.run(debug=True)