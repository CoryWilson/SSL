from flask import Flask, request, session, escape, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory
from werkzeug import secure_filename
import os
import hashlib
import mysql.connector

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True
sha1 = hashlib.sha1()

#function that checks user input with users in the database
def check_user(n,p):
     config = {
               'user':'root',
               'password':'root',
               'host':'127.0.0.1',
               'database':'ssl',
               'port':'8889'
          }

     db =  mysql.connector.connect(**config)
     cur = db.cursor()
     query = ('select username, password from users where username = %s and password = %s;')
     username = n
     password = sha1.update(p)
     pw_digest = sha1.hexdigest()
     cur.execute(query, (username, pw_digest))
     data = cur.fetchall()

     return data

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
     return render_template('body.html', data=data)

@app.route('/form')
def form():
     return render_template('/form.html')

@app.route('/login', methods=['GET','POST'])
#function that logs the user in
def login_check():
     if request.method == 'POST':
          #checks to see if form is empty and redirects home if it is
          if not request.form['name'] and not request.form['password']:
               return redirect(url_for('index'))
          #if everything checks out it processes the form
          else:
               input_name = request.form['name']
               input_password = request.form['password']
               returned_login = check_user(input_name,input_password)

               #if there is not correct log in info returned
               #redirect back to index
               if not returned_login:
                    return redirect(url_for('index'))
               else:
                    session['name'] =  returned_login[0][0]
                    session['password'] = returned_login[0][1]
                    name = session['name']
                    pw = session['password']

                    return render_template('/display.html',name=name,pw=pw)
               
     return redirect(url_for('index'))

@app.route('/logout')
#function that logs the user out
def logout():
     session.pop('name', None)
     session.pop('password', None)
     return redirect(url_for('form'))

@app.route('/display_user')
#function that displays the logged in user
def display_user():
     #if there is no session it will redirect back to login form
     if not session:
          return redirect(url_for('form'))
     else: 
          name = session['name']
          pw = session['password']
          return render_template('/display.html', name=name, pw=pw)

@app.route('/add_form')
#displays add form
def add_form():
     return render_template('add_form.html')

@app.route('/add_user', methods=['GET','POST'])
#adds user to database
def add_user():
     config = {
               'user':'root',
               'password':'root',
               'host':'127.0.0.1',
               'database':'ssl',
               'port':'8889'
          }

     db =  mysql.connector.connect(**config)
     cur = db.cursor()
     query = ('insert into users \
               (username,password) values (%s, %s);')
     username = request.form['name']
     password = request.form['password']
     new_password = sha1.update(password)
     pw_digest = sha1.hexdigest()
     cur.execute(query, (username, pw_digest))
     db.commit()
     return redirect('/')

@app.route('/delete_user/<id>', methods=['GET','POST'])
#deletes user from database
def delete_user(id):
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
     query = ('delete from users \
               where id = %s;')
     cur.execute(query, (id, ))
     db.commit()
     return redirect('/')

@app.route('/edit_form/<id>', methods=['GET', 'POST'])
#pulls up form for editing database entry
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
#updates database entry
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

#serves up the images from the uploads folder
@app.route('/uploads/<filename>')
def uploaded_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

      
if __name__ == '__main__':
     app.secret_key = 'JimBob'
     app.run()

