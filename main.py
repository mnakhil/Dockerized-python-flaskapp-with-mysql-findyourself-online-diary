from website import create_app
#from __init__ import db

app = create_app()



if __name__ == '__main__':
    #db.create_all() 
    app.run(debug=True,host="0.0.0.0") 
    