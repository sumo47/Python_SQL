# Importing the flask module
# import flask

# let's see the content of flask module
# print(dir(flask))

# importing the Flask class from flask module
from flask import Flask

# let's create the objet of the Flask class
app = Flask(__name__)

# First route: Index route/default route


@app.route('/')
def Index():

    # returning the response
    return "this is index page"

# Second route: Contact us


@app.route('/contact')
def contact():

    # returning the response
    return "This is contact page"

# Third route: About us


@app.route('/about')
def about():

    # returning the response
    return "This is about page"

# let's Run the flask Applicaton
app.run()