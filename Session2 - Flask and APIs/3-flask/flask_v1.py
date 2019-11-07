"""
This is an introduction to the flask framework which we can use to very easily
build our websites or web-apps with python. This script shows some of the basic
functionalities and functions you can use.

For more information on how flask works check out this link:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
Or watch this video:
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
"""

# import the flask package
from flask import Flask

# the only argument or variable that we have to pass  is the name of application
# this essentially tells flask where to find the application
app = Flask(__name__)



# routes and view functions:
# clients, such as a web browser, send requests to servers to get information
# when getting a website or computers do so directly, like in our API call
# earlier
# with our flask app we are making our own URL available, so we need to tell
# our app which code to run for which URl. This is done via the so-called
# routes. The '/' is the most basic route and indicates the start page, or index
# page
@app.route("/")
def index():
    return "Hello DSCS !"


@app.route("/user")
def user():
    return "Hello user"


@app.route("/user/<user_name>")
def user_nice(user_name):
    return "Hello {}!".format(user_name)


# Responses normally always include the status code 200, showing that everything
# is alright. sometimes we want our response to include a different status code
# than 200, in this case, we just return a tuple with the second variable being
# the status code
# Notice the status codes in your terminal indicating whether each load of
# the page was successful or not
@app.route("/bad-request-example")
def bad_request_example():
    return "No access, please try again", 401


# redirects
from flask import redirect

@app.route("/donate")
def donate():
    return redirect("https://www.msf.org")


# aborts
from flask import abort

@app.route("/error-example")
def error_example():
    abort(404)
    return "This wont work"


# combining this with our api requests
from api_module import fx_request
@app.route("/fx")
def fx_func():
    rate = fx_request()
    return "The exchange rate is {}".format(rate)


if __name__ == "__main__"   :
    app.run(debug=True, port=5000)
