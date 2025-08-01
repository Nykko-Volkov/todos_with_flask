import flask 
from db import Databases

app = flask.Flask(__name__)
decorator = app.route
todo_db = Databases('mytodo.db')
   
@decorator('/')
def ind():
    todos = todo_db.get_all()
    return flask.render_template('index.html',nathan_todo=todos)



@decorator('/save',methods=['post'])
def ind2():
    data = flask.request.form['inputfromhtml']
    todo_db.add(data)
    return flask.redirect('/')

@decorator('/delete/<path:todo>',methods=['post'])
def delete(todo):
    todo_db.delete(todo)
    return flask.redirect('/')

if __name__ == "__main__":
    app.run(debug=True)



