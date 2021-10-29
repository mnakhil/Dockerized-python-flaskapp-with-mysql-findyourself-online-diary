#from warnings import catch_warnings
from flask import Blueprint,render_template,flash,request
from flask_login import login_required,current_user
from flask_login.utils import _get_user

from .model import Diary
from . import db

views=Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html",user=current_user)

@views.route('/write', methods=['GET','POST'])
@login_required
def write():
    if request.method=='POST':
        data=request.form.get('data')
        privacy=request.form.get('privacy')
        user=_get_user()
        print(data)
        if len(data)<1:
            flash('The Diary entry is too short.',category="error")
        else:
            new_diary=Diary(data=data,privacy=privacy,name=user.firstName+" "+user.lastName,user_id=current_user.id)
            db.session.add(new_diary)
            db.session.commit()
            flash('The diary entry is saved.', category="success")
            
        

    return render_template("write.html", user=current_user)

@views.route('/account', methods=['GET','POST'])
@login_required
def account():
    return render_template("account.html", user=current_user)

@views.route('/feed')
@login_required
def feed():
    diary=Diary.query.filter_by(privacy='2').all()
    #print(diary[0].id)
    return render_template("feed.html",user=current_user,diaries=diary)