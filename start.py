from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/data.db"
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writingBox1=db.Column(db.Text)
    writingBox2=db.Column(db.Text)
    writingBox3=db.Column(db.Text)
    writingBox4=db.Column(db.Text)
    writingBox5=db.Column(db.Text)
    writingBox6=db.Column(db.Text)

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
    posts=Post.query.all()
    return render_template('about.html',title2=titleHeader,postList=posts)
@app.route("/pages")
def pages():
    return render_template('pages.html',title3=titleHeader)
@app.route("/service")
def service():
    return render_template('service.html',title4=titleHeader)
@app.route("/singleServices")
def singleServices():
    posts=Post.query.all()
    return render_template('singleServices.html',title5=titleHeader,postList=posts)
@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html',title6=titleHeader)





@app.route("/about/add",methods=["GET","POST"])
def aboutAdd():
    if request.method=='POST':
        post=Post(
        writingBox1=request.form['aboutbox1'],
        writingBox2=request.form['aboutbox2'],
        writingBox3=request.form['aboutbox3'],
        writingBox4=request.form['aboutbox4'],
        writingBox5=request.form['aboutbox5'],
        writingBox6=request.form['aboutbox6'])
        db.session.add(post)
        db.session.commit()
        redirect("/all")
    return render_template('admin/aboutAdd.html')
@app.route("/all")
def All():
    posts=Post.query.all()
    return render_template('admin/all.html',postList=posts)
@app.route("/about/delete/<int:id>")
def aboutDelete(id):
    postId=Post.query.get(id)
    db.session.delete(postId)
    db.session.commit()
    return redirect('/all')
@app.route("/about/update/<int:id>", methods=["GET","POST"])
def aboutUpdate(id):
    post=Post.query.get(id)
    if request.method=='POST':
        newWritingBox1=request.form['aboutbox1']
        newWritingBox2=request.form['aboutbox2']
        newWritingBox3=request.form['aboutbox3']
        newWritingBox4=request.form['aboutbox4']
        newWritingBox5=request.form['aboutbox5']
        newWritingBox6=request.form['aboutbox6']
        post.writingBox1=newWritingBox1
        post.writingBox2=newWritingBox2
        post.writingBox3=newWritingBox3
        post.writingBox4=newWritingBox4
        post.writingBox5=newWritingBox5
        post.writingBox6=newWritingBox6
        db.session.merge(post)
        db.session.flush()
        db.session.commit()
        return redirect("/all")
    return render_template('admin/aboutUpdate.html',post=post)
if __name__=='__main__':
    app.run(debug=True)