from flask import Blueprint,request,flash
from flask.templating import render_template

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html",boolean=True)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        secondName=request.form.get('lastName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        if len(email)<5:
            flash('Email must be greater than 4 charecters.',category="error")
        elif len(firstName)<3:
            flash('First name must be greater than 2 charectors.', category="error")
        elif len(secondName)<3:
            flash('Second name must be greater than 2 charectors.', category="error")
        elif password1!=password2:
            flash('Password missmatch.', category="error")
        elif len(password1)<7:
            flash('Password must be greater than 6 charectors.', category="error")
        else:
           flash('Account created.', category="success")   
    return render_template("signup.html",boolean=True)

@auth.route('/about')
def about():
    return render_template("about.html",boolean=True)