# Importing the flask module
# import flask

# let's see the content of flask module
# print(dir(flask))

# importing the Flask class from flask module
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# let's create the objet of the Flask class
app = Flask(__name__)

# connecting the flask app(server) with sqllite database
# let's write the uri: this command tells the flask app to connect with a sqllite type database named task.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'

# creating an object of SQLalchemy class
# Telling the SQLAlchemy class , which flask app to connect
database = SQLAlchemy(app)

# writing python class which will be used to insert data into table


class Task(database.Model):
    sno = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    description = database.Column(database.String(200), nullable=False)

# First route: Index route/default route


@app.route('/', methods=['GET', 'POST'])
def Index():

    # print(request.form)

    # let's check if the request is get or post
    # if request is post

    if request.method == 'POST':
        # FETCH the value of title and decription
        taskTitle = request.form.get('Title')
        taskDescription = request.form.get('Description')

        print(taskTitle, taskDescription)

        # add it to the database
        # creating row
        newTask = Task(title=taskTitle, description=taskDescription)
        database.session.add(newTask)
        database.session.commit()

        # returning the index.html page
        return redirect('/')
    else:
        # fetching all tasks from the database
        allTask = Task.query.all()

        print(allTask, type(allTask))

        # returning the response
        return render_template('index.html', allTask=allTask)

# Second route: Contact us


@app.route('/contact')
def contact():

    # returning the response
    return render_template('contact.html')

# Third route: About us


@app.route('/about')
def about():

    # returning the response
    return render_template('about.html')

# Delete task route


@app.route('/delete')
def delete():

    # extracting the sno
    sno = request.args.get('sno')

    # fetching task with sno = sno
    task = Task.query.filter_by(sno=sno).first()
    # print(task)

    # deleting the task
    database.session.delete(task)
    database.session.commit()

    return redirect('/')


    # let's Run the flask Applicaton
app.run(debug=True)
# app.run(debug=True, host='0.0.0.0')
