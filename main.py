
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, render_template, redirect, send_from_directory

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

############LANDING PAGE & INSTRUCTIONS##################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/socialmediadashboard")
def socialmediadashboard():
     return render_template("socialmediadashboard.html")

@app.route('/skillsdashboard')
def skillsdashboard():
     return render_template('skillsdashboard.html')

@app.route('/vacancydata')
def vacancydata():
     return render_template('vacancydata.html')

@app.route('/datasources')
def datasources():
    return render_template('datasources.html')