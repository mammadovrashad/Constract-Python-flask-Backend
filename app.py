from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager


app=Flask(__name__,template_folder='front')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/data.db"
db = SQLAlchemy(app)
migrate=Migrate(app,db)
manager=Manager(app)
manager.add_command('db',MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
@app.route("/")
def index():
    users=User.query.all()
    return render_template('home.html',userList=users)
@app.route("/add",methods=('GET','POST'))
def add():
    if request.method=='POST':
        username=request.form['ad']
        email=request.form['email']
        password=request.form['password']
        user=User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template('add.html ')
@app.route("/delete/<int:id>")
def delete(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")
@app.route("/update/<int:id>",methods=['POST','GET'])
def update(id):
    user1=User.query.get(id)
    if request.method=='POST':
        newname=request.form['ad']
        newemail=request.form['email']
        newpassword=request.form['password']
        user1.password=newpassword
        user1.username=newname
        user1.email=newemail 
        db.session.merge(user1)
        db.session.flush()
        db.session.commit()
        return redirect("/")
    else:
        return render_template('update.html',user1=user1)

if __name__=='__main__':
    app.run(debug=True)
    manager.run()