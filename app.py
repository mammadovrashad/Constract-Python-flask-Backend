from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,template_folder='front')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/data.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
@app.route("/")
def index():
    users=User.query.all()
    return render_template('home.html',userList=users)
@app.route("/add",methods=('POST','GET'))
def about():
    if request.method=='POST':
        username=request.form['ad']
        email=request.form['email']
        user=User(username=username,email=email)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('add.html')


@app.route("/delete/<int:id>")
def delete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:id>",methods=('POST','GET'))
def update(id):
    user=User.query.get(id)
    if request.method=='POST':
        newUsername=request.form["ad"]
        newEmail=request.form["email"]
        user.username=newUsername
        user.email=newEmail
        db.session.merge(user)
        db.session.flush()
        db.session.commit()
        return redirect("/")
    else:
        return render_template("update.html" ,user=user)
if __name__=='__main__':
    app.run(debug=True)