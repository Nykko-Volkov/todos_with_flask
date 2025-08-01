import flask 
from flask import Flask, render_template,request,redirect
from db import Databases

app = Flask(__name__)
decorator = app.route
todo_db = Databases('mytodo.db')
   
@decorator('/')
def ind():
    todos = todo_db.get_all()
    return render_template('index.html',nathan_todo=todos)



@decorator('/save',methods=['post'])
def ind2():
    data = request.form['inputfromhtml']
    todo_db.add(data)
    return redirect('/')

@decorator('/delete/<path:todo>',methods=['post'])
def delete(todo):
    todo_db.delete(todo)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



