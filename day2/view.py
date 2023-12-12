from flask import Flask, request, redirect,url_for, session, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app=Flask(__name__)

app.secret_key = 'secret_key'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Extention@1'
app.config['MYSQL_DB']='userprofile'

mysql=MySQL(app)

@app.route('/login',methods=['GET','POST'])
def login():
    message=''
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        username=request.form['username']
        password=request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('Select * from user where username = %s and password =%s',(username,password))
        user=cursor.fetchone()
        if user:
            session['loggedin']=True
            session['id']=user['id']
            session['username']=user['username']
            message='login successful'
            return render_template('home.html',message=message)
        else:
            message='invalid credentials'
            return render_template('login.html',message=message)

    
    return render_template('login.html')



if __name__=="__main__":
    app.run(host='0.0.0.0',port='85',debug=True)