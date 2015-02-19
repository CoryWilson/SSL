from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	print 'hello'
	return 'browser'

@app.route('/loginForm')
def loginForm():
	return render_template('/loginForm.html')

@app.route('/processForm/<userid>', methods=['GET','POST'])
def processForm(userid):
	return userid
	# return request.form["firstname"]

app.Debug = True

if __name__ == '__main__':
	app.run()

