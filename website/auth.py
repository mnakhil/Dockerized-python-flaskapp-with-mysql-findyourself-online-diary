from flask import Blueprint,request,flash,redirect,url_for
from flask.templating import render_template


from .model import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user
auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        print(email)
        if len(email)<6:
            flash('Email must have more than 5 letters',category='error')
        user= User.query.filter_by(email=email).first() 
        #user=db.session.query(User).filter(User.email==email)
        #print(user.email)
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully.', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.feed'))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email does not exists, please singn up to access your account.', category='error')
    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        lastName=request.form.get('lastName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        secQuestion=request.form.get('question')
        answer=request.form.get('answer')
        user= User.query.filter_by(email=email).first()
        print(email)
        #print(user.email)
        if user:
            flash('User already exists, Please try loggin into your account.',category='error')
        elif len(email)<5:
            flash('Email must be greater than 4 charecters.',category="error")
        elif len(firstName)<3:
            flash('First name must be greater than 2 charectors.', category="error")
        elif len(lastName)<3:
            flash('Second name must be greater than 2 charectors.', category="error")
        elif password1!=password2:
            flash('Password missmatch.', category="error")
        elif len(password1)<7:
            flash('Password must be greater than 6 charectors.', category="error")
        else:
            new_user=User(email=email,firstName=firstName,secQuestion=secQuestion,answer=answer,lastName=lastName,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created.', category="success")   
            #login_user(user,remember=True)
            return redirect(url_for('auth.login'))
    return render_template("signup.html",user=current_user)

@auth.route('/forgotPass',methods=['POST','GET'])
def forgotPass():
    if request.method=='POST':
        email=request.form.get('email')
        secQuestion=request.form.get('question')
        answer=request.form.get('answer')
        user= User.query.filter_by(email=email).first()
        print(secQuestion)
        print(user.secQuestion)
        if user:
            if user.secQuestion==secQuestion and user.answer==answer:
                return redirect(url_for('auth.updatePass',user=user.id))
            else:
                flash('Quetion and answer does not match.',category="error")
        else:
            flash('User does not exists.',category="error")
    return render_template('forgotPass.html',user=current_user)

@auth.route('/updatePass', methods=['GET','POST'])
def updatePass():
    if request.method=='POST':
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        if(password1!=password2):
            flash("Entered passwords mismatch.",category='error')
        elif(len(password1)<7):
            flash("Password must be greater than 6 letters.", category="error")
        else:
            userid=request.args.get('user')
            user=User.query.filter_by(id=userid).first()
            user.password=generate_password_hash(password1, method='sha256')
            db.session.commit()
            flash('Password reset successful.','success')
            return redirect(url_for('auth.login'))
    return render_template("updatePass.html",user=current_user)

