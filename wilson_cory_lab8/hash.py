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


@app.route('/')
def index():
     return render_template('/form.html')
@app.route('/form')
def form():
     return render_template('/form.html')

@app.route('/login', methods=['GET','POST'])
def login_check():
     if request.method == 'POST':
          session['name'] = request.form['name']
          #return redirect(url_for('index'))
          return redirect(url_for('display_all'))
     return render_template('/form.html')

# def login_check():
#      if returned_login:
#           session['name'] = request.form['name']
#      #      session['loggedin'] = True
#      # else:
#      #      session['name'] = ""
#      #      session['loggedin'] = false
#      print returned_login
#      return render_template('/display.html',returned_login=returned_login)

@app.route('/logout')
def logout():
     session.pop('name', None)
     return redirect(url_for('index'))

def check_user(user):
     config = {
               'user':'root',
               'password':'root',
               'host':'127.0.0.1',
               'database':'ssl',
               'port':'8889'
          }

     db =  mysql.connector.connect(**config)
     cur = db.cursor()
     query = ('select id, username, password from users where username = %s and password = %s;')
     #username = request.form["name"]
     username = user["name"]
     #password = sha1.update(request.form["password"])
     password = sha1.update(user["password"])
     pw_digest = sha1.hexdigest()
     cur.execute(query, (username, pw_digest))
     data = cur.fetchall()

     #return render_template('/display.html',data=data)
     return data

# @app.route('/display_user')
# def display_user():
#      data = session
#      return render_template('/display.html',data=data)


@app.route('/display_all')
def display_all():
     config = {
               'user':'root',
               'password':'root',
               'host':'127.0.0.1',
               'database':'ssl',
               'port':'8889'
          }

     db =  mysql.connector.connect(**config)
     cur = db.cursor()
     query = ('select id, username, password from users;')
     cur.execute(query)
     data = cur.fetchall()

     return render_template('/display.html',data=data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

      
if __name__ == '__main__':
     app.secret_key = 'JimBob'
     app.run()

