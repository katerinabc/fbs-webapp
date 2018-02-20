
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, redirect, send_from_directory
from flask.ext.navigation import Navigation

app = Flask(__name__)
nav = Navigation(app)

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

############LANDING PAGE & INSTRUCTIONS##################
nav.Bar('top', [
    nav.Item('Home', 'Dashboard', 'Data Collection', 'Human Capital Strategy'),
])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/socialmediadashboard")
def socialmediadashboard():
     return render_template("socialmediadashboard.html")

@app.route('/skillsdashboard')
def skillsdashboard():
     return render_template('skillsdashboard.html')

@app.route('/datasource')
def datasorce():
     return render_template('datasource.html')

@app.route('/vacancydata')
def vacancydata():
     return render_template('vacancydata.html')

@app.route('/downloaddata')
def downloaddata():
    return render_template('downloaddata.html')
