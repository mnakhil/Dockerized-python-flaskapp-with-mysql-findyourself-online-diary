#from warnings import catch_warnings
from re import template
from flask import Blueprint,render_template,flash,request,jsonify
from flask.helpers import url_for
from flask_login import login_required,current_user
from flask_login.utils import _get_user
import json
from sqlalchemy.orm import session

from werkzeug.utils import redirect
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

@views.route('/deleteEntry', methods=['POST'] )
@login_required
def deleteEntry():
    entry=json.loads(request.data)
    noteId=entry['noteId']
    note=Diary.query.get(noteId)
    print(note)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/updateEntry/<int:id>', methods=['POST','GET'] )
@login_required
def updateEntry(id):
    #entry=json.loads(request.data)
    
    note=Diary.query.filter_by(id=id).first()
    print(note.name)
    if note:
        if note.user_id==current_user.id:
            return redirect(url_for('views.update',id=note.id,user=current_user))
    return flash("Update Your data here.",category="success")




@views.route('/update', methods=['POST', 'GET'])
@login_required
def update():
    #entry=Diary.query.get(id)
    data=int(request.args.get('id'))
    entry=Diary.query.filter_by(id=data).first()
    print(entry.data)
    
    print(entry.name)
    if request.method=='POST':
        
        data=request.form.get('data')
        privacy=request.form.get('privacy')
        
        if len(data)<1:
            flash('The Diary entry is too short.',category="error")
        else:
            entry.data=data
            entry.privacy=privacy
            db.session.commit()
            flash('Diary updated.',category='success')
            return render_template('account.html',user=current_user)
    return render_template('update.html',user=current_user,entryid=entry)

@views.route('/forgotPass')
def forgotPass():
    return render_template("forgotPass.html",user=current_user)

@views.route('/about')
def about():
    return render_template("about.html",user=current_user)