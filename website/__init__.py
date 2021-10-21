from flask import Flask

def creat_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="13A31M01N"
    return app
        