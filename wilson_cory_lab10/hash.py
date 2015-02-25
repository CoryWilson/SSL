from flask import Flask, request, session, escape, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory, jsonify
from werkzeug import secure_filename
import os, hashlib, mysql.connector, urllib, json

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.debug = True
sha1 = hashlib.sha1()

# @app.route('/')
# def get_json():
#      api_key_b = "AIzaSyCy3kAz1R6WFKNrSL0wqE0qVcJwd9HSzJ4"
#      api_key_s = "AIzaSyCiXjaUwDAUVQpMtsKYFahB2q7dzNolXYY"
#      url = "https://maps.googleapis.com/maps/api/directions/json?origin=Orlando,FL&destination=Los+Angeles,CA&key="+api_key_b
#      loadurl = urllib.urlopen(url)
#      data = json.loads(loadurl.read().decode(loadurl.info().getparam('charset') or 'utf-8'))
#      start = data['routes'][0]['legs'][0]['start_address']
#      end = data['routes'][0]['legs'][0]['end_address']
#      distance = data['routes'][0]['legs'][0]['distance']['text']
#      duration = data['routes'][0]['legs'][0]['duration']['text']
#      return render_template('json_body.html',start=start,end=end,distance=distance,duration=duration)

@app.route('/')
def form():
     return render_template('/form.html')

@app.route('/submit_info', methods=['GET','POST'])
def submit_info():
     api_key_b = "AIzaSyCy3kAz1R6WFKNrSL0wqE0qVcJwd9HSzJ4"
     api_key_s = "AIzaSyCiXjaUwDAUVQpMtsKYFahB2q7dzNolXYY"

     start_city_input = request.form['start_city']
     start_state_input = request.form['start_state']
     end_city_input = request.form['end_city']
     end_state_input = request.form['end_state']
     start_input = start_city_input+','+start_state_input
     end_input = end_city_input+','+end_state_input

     url = "https://maps.googleapis.com/maps/api/directions/json?origin="+start_input+"&destination="+end_input+"&key="+api_key_b
     #url = "https://maps.googleapis.com/maps/api/directions/json?origin=Orlando,FL&destination=Los+Angeles,CA&key="+api_key_b
     
     loadurl = urllib.urlopen(url)
     data = json.loads(loadurl.read().decode(loadurl.info().getparam('charset') or 'utf-8'))
     
     start = data['routes'][0]['legs'][0]['start_address']
     end = data['routes'][0]['legs'][0]['end_address']
     start_lat = data['routes'][0]['legs'][0]['start_location']['lat']
     start_lng = data['routes'][0]['legs'][0]['start_location']['lng']
     end_lat = data['routes'][0]['legs'][0]['end_location']['lat']
     end_lng = data['routes'][0]['legs'][0]['end_location']['lng']
     distance = data['routes'][0]['legs'][0]['distance']['text']
     duration = data['routes'][0]['legs'][0]['duration']['text']
     polyline = data['routes'][0]['overview_polyline']['points']
     return render_template('json_body.html',start=start,end=end,distance=distance,duration=duration, start_lat=start_lat,start_lng=start_lng,end_lat=end_lat,end_lng=end_lng)

#serves up the images from the uploads folder
@app.route('/uploads/<filename>')
def uploaded_file(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

      
if __name__ == '__main__':
     app.secret_key = 'JimBob'
     app.run()

