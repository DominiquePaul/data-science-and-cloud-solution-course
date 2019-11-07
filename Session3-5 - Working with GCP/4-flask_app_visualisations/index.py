"""
Adding a nicer design to our app and make it navigatable

To run the script you might have to run the following commands in your terminal
first. If you have installed python with anaconda then replace 'pip' with 'conda'

pip install Flask-WTF
pip install WTForms
pip install flask-bootstrap
"""

# import the flask package
from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
# we load the bootstrap extension so we can use it in our app
# bootstrap = Bootstrap(app)
# To use forms we have to set a secret configuration key for the flask app.
app.config["SECRET_KEY"] = "a-very-secret-password"


# dont save an api keys in your applications, instead use environment variables.
WEATHER_API_KEY = "YOUR_API_KEY"


# to use a form we have to define a class of the form
class NameForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/form', methods=['GET', 'POST'])
def form_func():
    name = ""
    # we call the form class that we defined earler here
    form = NameForm()
    # this condition checks whether the data was submitted
    if form.validate_on_submit():
        name = form.name.data
        # this clears the field after submission back to an empty state
        form.name.data = ''

    return render_template('form1.html', form=form, name=name)

@app.route('/weather')
def weather():
    city="Berlin"
    temp = helper_weather(city)
    return render_template("weather.html", city=city, temperature=temp)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


def helper_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
     "q": city,
     "appid": WEATHER_API_KEY,
     "units": "metric"
    }

    r = requests.get(url,params=params)
    temperature = r.json()["main"]["temp"]

    return temperature





# this command only runs when the script itself is being executed and not, for
# example when this script is loaded by another package
if __name__ == "__main__"   :
    app.run(debug=True, host="0.0.0.0", port=5000)
