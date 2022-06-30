from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import visualizations

@app.route("/")
def index():

if __name__ == "__main__":
   app.run(debug=False, use_reloader=False)