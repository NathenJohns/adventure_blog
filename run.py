import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'adventure_blog'
app.config["MONGO_URI"] = 'mongodb://Nathen:woodstock21@ds145194.mlab.com:45194/adventure_blog'

mongo = PyMongo(app)

# HOME NAVIGATION
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

# ABOUT NAVIGATION
@app.route('/about')
def about():
    return render_template("about.html")

# GET ARTICLES NAVIGATION
@app.route('/articles')
def get_articles():
    return render_template("articles.html", articles=mongo.db.articles.find())

# GET COUNTRIES NAVIGATION
@app.route('/countries')
def get_countries():
    return render_template("countries.html", countries=mongo.db.countries.find())
    
# ADDING ARTICLES AND COUNTRIES

@app.route('/write_article')
def write_article():
    return render_template("write_article.html",
    articles=mongo.db.articles.find())
    
@app.route('/insert_article', methods=['POST'])
def insert_article():
    articles = mongo.db.articles
    articles.insert_one(request.form.to_dict())
    return redirect(url_for('get_articles'))

@app.route('/add_country')
def add_country():
    return render_template("add_country.html", locations=mongo.db.locations.find(), risks=mongo.db.risks.find())

@app.route('/insert_country', methods=['POST'])
def insert_country():
    countries = mongo.db.countries
    countries.insert_one(request.form.to_dict())
    return redirect(url_for('get_countries'))

# EDITING ARTICLES AND COUNTRIES

@app.route('/edit_country/<country_id>')
def edit_country(country_id):
    the_country = mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template('edit_country.html', country=the_country, locations=mongo.db.locations.find(), risks=mongo.db.risks.find())

@app.route('/update_country/<country_id>', methods=['POST'])
def update_country(country_id):
    mongo.db.countries.update(
        {'_id': ObjectId(country_id)},
        {
            "country_name": request.form.get('country_name'),
            "country_location": request.form.get('country_location'),
            "country_currency": request.form.get('country_currency'),
            "country_risk": request.form.get('country_risk'),
            "country_language": request.form.get('country_language'),
            "injections": request.form.get('injections'),
            "country_description": request.form.get('country_description'),
            "reasons_to_go": request.form.get('reasons_to_go')
        })
    return redirect(url_for('get_countries'))

# DELETING ARTICLES AND COUNTRIES
@app.route('/delete_article/<article_id>')
def delete_article(article_id):
    mongo.db.articles.remove({'_id': ObjectId(article_id)})
    return redirect(url_for('get_articles'))
    
@app.route('/delete_country/<country_id>')
def delete_country(country_id):
    mongo.db.countries.remove({'_id': ObjectId(country_id)})
    return redirect(url_for('get_countries'))

# SINGLE ARTICLE
@app.route('/article/<article_id>')
def single_article(article_id):
    article=mongo.db.articles.find_one({'_id': ObjectId(article_id)})

    return render_template('single_article.html', article=article)

# SINGLE COUNTRY
@app.route('/country/<country_id>')
def single_country(country_id):
    country=mongo.db.countries.find_one({'_id': ObjectId(country_id)})

    return render_template('single_country.html', country=country)
    
# SIGN UP
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)