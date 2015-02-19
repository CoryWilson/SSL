from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from werkzeug.security import generate_password_hash
import hashlib
import mysql.connector

app = Flask(__name__)
app.secret_key = 'cory'

@app.route('/')
def index():
	print 'hello'
	return 'browser'

@app.route('/loginForm')
def loginForm():
	return render_template('/loginForm.html')

@app.route('/processForm/<userid>', methods=['GET','POST'])
def processForm(userid):

	db =  mysql.connector.connect(user='root',password='root',host='127.0.0.1',database='ssl',port='8889')
	cur = db.cursor()
	cur.execute('select username, password from users')
	data = cur.fetchall()
	#redirect ("/loginForm")

	#data = []
	#newid = generate_password_hash(userid)
	return render_template('body.html', data=data)
	# return request.form["firstname"]

app.Debug = True

if __name__ == '__main__':
	app.run()

# insert into users values ('','joe','123','')


#redirect, session, form, get, post, hash, select
#pass parameters into statement
#send to info or redirect to login