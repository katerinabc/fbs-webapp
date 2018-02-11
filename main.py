#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:29:04 2017

@author: guysimons
"""

import os
from flask import Flask, request, render_template, redirect, send_from_directory

os.chdir('/Users/katerinadoyle/Documents/gitrepo/fbswebapp')


############DEFINE WEB APP VARIABLES##################
app = Flask(__name__)



############LANDING PAGE & INSTRUCTIONS##################
@app.route("/")
def index():
    return render_template("main.html")

@app.route("/socialmediadashboard")
def socialmediadashboard():
     return render_template("socialmediadashboard.html")

@app.route('/skillsdashboard')
def skillsdashboard():           
     return render_template('skillsdashboard.html')

@app.route('/vacancydata')
def vacancydata():           
     return render_template('vacancydata.html')

@app.route('/downloaddata')
def downloaddata():           
     return render_template('downloaddata.html')

if __name__ == "__main__":
    app.run(port = 5002)


