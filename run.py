import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'adventure_blog'
app.config["MONGO_URI"] = 'mongodb://Nathen:woodstock21@ds145194.mlab.com:45194/adventure_blog'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/articles')
def get_articles():
    return render_template("articles.html", articles=mongo.db.articles.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)