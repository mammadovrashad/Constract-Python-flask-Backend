from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
app = Flask(__name__)

titleHeader='header'
titleAbout='about'
titlePages='pages'
titleService='service'
titleSingleServices='singleServices'
titlePortfolio='portfolio'
@app.route("/")
def header():
    return render_template('header.html',title1=titleHeader)
@app.route("/about")
def about():
    return render_template('about.html',title2=titleHeader)
@app.route("/pages")
def pages():
    return render_template('pages.html',title3=titleHeader)
@app.route("/service")
def service():
    return render_template('service.html',title4=titleHeader)
@app.route("/singleServices")
def singleServices():
    return render_template('singleServices.html',title5=titleHeader)
@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html',title6=titleHeader)


if __name__=='__main__':
    app.run(debug=True)