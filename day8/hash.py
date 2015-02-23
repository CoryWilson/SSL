from flask import Flask, request, session, escape, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory
from werkzeug import secure_filename
import os
import hashlib
import mysql.connector

app = Flask(__name__)

app.Debug = True

@app.route('/')
def index():
	config = {
		'user':'root',
		'password':'root',
		'host':'127.0.0.1',
		'database':'ssl',
		'port':'8889'
	}
	db = mysql.connector.connect(**config)
	cur = db.cursor()
	query = ('select id, username, password from users')
	cur.execute(query)
	data = cur.fetchall()
	print data
	return render_template('body.html', data=data)

# @app.route('/process_form/<userid>', methods=['GET', 'POST'])
# def process_form(userid):
# 	data = []
# 	sha1 = hashlib.sha1()
# 	sha1.update(request.form["firstname"])
# 	data.apend(sha1.hexdigest())
# 	return render_template('body.html',data=data)

@app.route('/edit_form/<id>', methods=['GET', 'POST'])
def edit_form(id):
	id = id
	config = {
		'user':'root',
		'password':'root',
		'host':'127.0.0.1',
		'database':'ssl',
		'port':'8889'
	}
	db =  mysql.connector.connect(**config)
	cur = db.cursor()
	query = ('select id, username, password from users where id=%s');
	cur.execute(query, (id, ))
	data = cur.fetchall()
	return render_template('edit_form.html', data=data)

@app.route('/update_user/<id>', methods=['GET', 'POST'])
def update_user(id):
	id = id
	username = request.form["username"]
	print username
	config = {
		'user':'root',
		'password':'root',
		'host':'127.0.0.1',
		'database':'ssl',
		'port':'8889'
	}
	db =  mysql.connector.connect(**config)
	cur = db.cursor()
	query = ('update users set username = %s where id = %s')
	cur.execute(query, (username, id))
	db.commit()
	return redirect('/')

#add_form, add_user, and delete_user
#delete and add need commit
@app.route('/add_form')
def add_form():
	return "something"

@app.route('/add_user')
def add_user():
	return "something"

@app.route('/delete_user/<id>')
def delete_user(id):
	return "something"

if __name__ == '__main__':
	app.run()

