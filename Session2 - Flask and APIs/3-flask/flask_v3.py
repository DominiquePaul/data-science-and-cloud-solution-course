"""
In this script we will look at how we can get user input for our app. This for
example can be useful, when we want to customise the response that we want to
return or when we want a user to log in

For more information on how flask forms work check out this link:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
Or watch this video:
https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3

To run the script you might have to run the following commands in your terminal
first. If you have installed python with anaconda then replace 'pip' with 'conda'

pip install Flask-WTF
pip install WTForms
"""

# import the flask package
from flask import Flask, render_template, flash, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


# the only argument or variable that we have to pass  is the name of application
# this essentially tells flask where to find the application
app = Flask(__name__)

# To use forms we have to set a secret configuration key for the flask app.
# All you have to know for now is that this is a security measure and that we
# wont need to use or interact with it in the remainder of the script, so you
# can more or less ignore it
app.config["SECRET_KEY"] = "a-very-secret-password"


# we again include the index route
@app.route("/")
def index():
    return "Hello DSCS"


# to use a form we have to define a class of the form
class NameForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')


# for the form route we now include the 'methods' parameter which tells the
# program which type of call are allowed. 'GET' is what we have been using before
# by default. 'POST' means that the user or rather the URL we are accessing can
# also send information back to us
@app.route('/form', methods=['GET', 'POST'])
def form_func():
    name = None
    # we call the form class that we defined earler here
    form = NameForm()
    # this condition checks whether the data was submitted
    if form.validate_on_submit():
        name = form.name.data
        # this clears the field after submission back to an empty state
        form.name.data = ''

    return render_template('form1.html', form=form, name=name)



# this command only runs when the script itself is being executed and not, for
# example when this script is loaded by another package
if __name__ == "__main__"   :
    app.run(debug=True, port=5000)
