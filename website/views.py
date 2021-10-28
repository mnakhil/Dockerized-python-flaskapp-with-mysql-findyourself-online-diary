#from warnings import catch_warnings
from flask import Blueprint,render_template,flash,request
from flask_login import login_required,current_user

from .model import Diary
from . import db

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html",user=current_user)

@views.route('/account', methods=['GET','POST'])
@login_required
def account():
    if request.method=='POST':
        data=request.form.get('data')
        print(data)
        if len(data)<1:
            flash('The Diary entry is too short.',category="error")
        else:
            new_diary=Diary(data=data,user_id=current_user.id)
            db.session.add(new_diary)
            db.session.commit()
            flash('The diary entry is saved.', category="success")
            
        

    return render_template("account.html", user=current_user)
