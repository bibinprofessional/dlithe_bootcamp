
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

def find_user(username,phone):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('Select username,phone from user')
    user=cursor.fetchall()
    for i in user:
        if i['username']==username or str(i['phone'])==phone:
            return False
        
    else:
        return True
    
def check_other_user(username,phone,user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('Select id,username,phone from user')
    user=cursor.fetchall()
    for i in user:
        if (i['username']==username or str(i['phone'])==phone) and i['id']!=user_id:
            return False
        
    else:
        return True
    
def check_user(user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('Select * from user')
    user=cursor.fetchall()
    for i in user:
        if i['id']==user_id:
            return i
        
    else:
        return False


    
@app.route('/register',methods=['GET','POST'])
def register():
    message=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        email=request.form['email']
        phone=request.form['phone']
        address=request.form['address']
        city=request.form['city']
        state=request.form['state']
        country=request.form['country']
        postcode=request.form['postcode']

        if find_user(username,phone):

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('insert into user (username,password,email,phone,address,city,state,country,postcode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(username,password,email,phone,address,city,state,country,postcode))
            mysql.connection.commit()
            
            return redirect('/login')
        
        else:
            message='username or phone already exist'
            return render_template('register.html',message=message)

    return render_template('register.html')



if __name__=="__main__":
    app.run(host='0.0.0.0',port='85',debug=True)