"""
This script is not the official start of the flask moduel but just serves to
show how easy it can be to set-up a very small flask app and get started

To run the script you might have to run the following commands in your terminal
first. If you have installed python with anaconda then replace 'pip' with 'conda'

pip install flask
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
    return "Hello DSCS"


# this command only runs when the script itself is being executed and not, for
# example when this script is loaded by another package
if __name__ == "__main__"   :
    app.run(debug=True, port=5000)
