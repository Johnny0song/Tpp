from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache()
def init_ext(app):
    db.init_app(app)
    migrate.init_app(app=app,db=db)
    mail.init_app(app)
    cache.init_app(app=app,config={'CACHE_TYPE':'simple'})