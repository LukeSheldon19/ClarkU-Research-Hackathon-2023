from flask import Flask, Blueprint, render_template, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("home.html")
    
@views.route("/views/")
def home2():
    return render_template("index.html")

