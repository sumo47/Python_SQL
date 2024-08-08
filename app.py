
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'

database = SQLAlchemy(app)


class Task(database.Model):
    sno = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    description = database.Column(database.String(200), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def Index():

    if request.method == 'POST':
        taskTitle = request.form.get('Title')
        taskDescription = request.form.get('Description')

        print(taskTitle, taskDescription)

        newTask = Task(title=taskTitle, description=taskDescription)
        database.session.add(newTask)
        database.session.commit()

        return redirect('/')
    else:
        allTask = Task.query.all()

        print(allTask, type(allTask))

        return render_template('index.html', allTask=allTask)



@app.route('/contact')
def contact():

    return render_template('contact.html')



@app.route('/about')
def about():

    return render_template('about.html')



@app.route('/delete')
def delete():

    sno = request.args.get('sno')

    task = Task.query.filter_by(sno=sno).first()
    database.session.delete(task)
    database.session.commit()

    return redirect('/')



@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        sno = request.args.get('sno')
        task = Task.query.filter_by(sno=sno).first()

        return render_template('update.html', task=task)

    else:

        sno = request.args.get('sno')
        title = request.form.get('Title')
        description = request.form.get('Description')
        # updating databse/task
        task = Task.query.filter_by(sno=sno).first()
        task.title = title
        task.description = description

        database.session.add(task)
        database.session.commit()

        return redirect('/')


