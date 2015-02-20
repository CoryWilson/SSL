import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory
from werkzeug import secure_filename
import hashlib
from werkzeug.security import generate_password_hash
import mysql.connector

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True

@app.route('/')
def index():
	return render_template('/form.html')

@app.route('/form')
def loginForm():
	return render_template('/form.html')

@app.route('/process_form', methods=['GET','POST'])
def process_form():
     if request.method == 'POST':

          data = []

          sha1 = hashlib.sha1()

          name = request.form["name"]
          password = request.form["password"]
          
          new_password = sha1.update(password)

          digest = sha1.hexdigest()

          f = request.files['file']
          f.save('./uploads/'+f.filename)

          img_url = './uploads/'+f.filename       

          data.append(name)
          data.append(digest)
          data.append(img_url)

     return render_template('/display.html',data=data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

      
if __name__ == '__main__':
  app.run()

