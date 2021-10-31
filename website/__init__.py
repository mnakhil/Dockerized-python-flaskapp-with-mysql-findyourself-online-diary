from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from os import path
# from flask_mysqldb import MySQL
from sqlalchemy_utils.functions.database import create_database
#from . import app
from flask_login import LoginManager

db = SQLAlchemy()




def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="13A31M01N"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@db/diarydb"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['MYSQL_HOST']='127.0.0.1:3307'
    # app.config['MYSQL_USER']='root'
    # app.config['MYSQL_PASSWORD']='133101mys0l'
    # app.config['MY']
    db.init_app(app)
    #db.create_all()
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .model import User,Diary
    
    # create_db(app)
    # with app.app_context():
    #     db.create_all()
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# def create_db(app):
#     if not database_exists('mysql://root:133101mys0l@127.0.0.1:3307/'+DB_NAME):
#         create_database('mysql://root:133101mys0l@127.0.0.1:3307/'+DB_NAME)
#         with app.app_context():
#             db.create_all()
#         print("Database created.")


