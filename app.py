import flask 
from db import Databases

app = flask.Flask(__name__)
decorator = app.route
todos = ['sleep on time', 'wake up on time', 'eat properly', 'study', 'work']
   
@decorator('/')
def ind():
    return flask.render_template('index.html',nathan_todo=todos)



@decorator('/save',methods=['post'])
def ind2():
    data = flask.request.form['inputfromhtml']
    todos.append(data)
    return flask.redirect('/')

@decorator('/delete/<path:todo>',methods=['post'])
def delete(todo):
    if todo in todos:
        todos.remove(todo)
    return flask.redirect('/')


app.run(debug=True)



