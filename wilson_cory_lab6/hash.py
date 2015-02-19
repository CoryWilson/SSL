import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory
from werkzeug import secure_filename
import hashlib
from werkzeug.security import generate_password_hash
import mysql.connector


UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['jpg','jpeg','png','gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.debug = True

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
	return render_template('/layout.html')

@app.route('/loginForm')
def loginForm():
	return render_template('/loginForm.html')

@app.route('/processForm/<userid>', methods=['GET','POST'])
def processForm(userid):
  data = []
  # sha1=hashlib.sha1()
  # newid = sha1.update("test")

  # data.append(newid.sha1.hexdigest())

  newid = generate_password_hash(userid)

  data.append(newid)
  data.append[request.form["name"]]
  data.append[request.form["password"]]

  # if request.method == 'POST':
  #   file = request.files['file']
  #   if file and allowed_file(file.filename):
  #     filename = secure_filename(file.filename)
  #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  #     return redirect(url_for('uploaded_file', filename=filename))
  return render_template(data=data)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/display')
def display():
	return render_template('/display.html')
      
if __name__ == '__main__':
  app.run()

