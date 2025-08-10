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
    if 'username' not in session:
        return redirect('/signin')
    username = session['username']

    todos = todo_db.get_all_posts(username)
    print(todos)
    
    return render_template('index.html',nathan_todo=todos,user=username)


@decorator('/save',methods=['post'])
def ind2():
    username =''
    if 'username' in session:
        username = session['username']
    else:
        redirect('/signin')
    data = request.form['inputfromhtml']
    todo_db.add(data,username)
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
        all_users = todo_db.get_user(un)
        if un in all_users:
            return 'Username already exists'

        todo_db.add_user(un,up)
        del session['username']
        session['username'] = un
        return redirect('/')
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
                return redirect('/')
        else:
            'username not found'
    return render_template('signin.html')

@decorator('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signin')



if __name__ == "__main__":
    app.run(debug=True)



