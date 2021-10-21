from flask import Blueprint
from flask.templating import render_template

auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html",boolean=True)

