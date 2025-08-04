import flask 
from flask import Flask, render_template,request,redirect, session
from db import Databases

users = {'nathan':'1234'}

app = Flask(__name__)
app.secret_key = '0009090'
decorator = app.route
todo_db = Databases('mytodo.db')
   
@decorator('/')
def ind():
    todos = todo_db.get_all_posts()
    return render_template('index.html',nathan_todo=todos,users=users)


@decorator('/save',methods=['post'])
def ind2():
    data = request.form['inputfromhtml']
    todo_db.add(data)
    return redirect('/')

@decorator('/delete/<path:todo>',methods=['post'])
def delete(todo):
    todo_db.delete(todo)
    return redirect('/')

@decorator('/signup',methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        un = request.form['uname']
        up = request.form['upass']
        todo_db.add_user(un,up)
        redirect('/')
    return render_template('signup.html')
    

@decorator('/signin',methods = ['GET','POST'])
def signin():
    if request.method == "POST":
        un = request.form['uname']
        up = request.form['upass']
        user = todo_db.get_user(un)
        if user:
            if user[1] == up:
                session['username'] = up
        else:
            '~username not found'
    return render_template('signin.html')

if __name__ == "__main__":
    app.run(debug=True)



