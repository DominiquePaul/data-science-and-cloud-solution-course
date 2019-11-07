"""
This script introduces to using html forms instead of just returning either
plain strings or html files in the same document. Additionally, it also shows
how you can dynamically display content based on basic if-conditions or for-loops

For more information on how flask templates work check out this link:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
Or watch this video:
https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2
"""

# import the flask package
from flask import Flask

# the only argument or variable that we have to pass  is the name of application
# this essentially tells flask where to find the application
app = Flask(__name__)



@app.route("/")
def index():
    return "Hello DSCS"



# using templates
# we could add own variables to our web templates like this, but this wouldnt
# be a very nice format and there would be issues for larger files
@app.route('/index')
def ugly_template():
    users = {'user_name': 'Dominique'}
    return """
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Bonjour """ + users['user_name'] + """!</h1>
            </body>
        </html>"""



# instead we can save html files in a folder that we call 'templates' and call
# use the render_template function to return these instead. This allows us to
# cleanly separate the code. At the same time, we can still pass on content to
# the template as we are doing here. Can you see how the variables 'company_name'
# and 'user' are used in the index1.html file?
# This is done by using the jinja2 web template format
from flask import render_template

@app.route('/index1')
def nicer_template():
    users = {'user_name': 'Dominique'}
    return render_template('index1.html', company_name='Nostos Genomics', user=users)



# we can even use logical structures like if-clauses, similar to python. Have a
# look at the index2.html file and try and understand what is happening
@app.route('/index2')
def smart_template():
    users = {'user_name': 'Dominique'}
    return render_template('index2.html', company_name='Nostos Genomics')



# we can by the same terms also use a for loop to format the output of a list
@app.route('/index3')
def smart_template2():
    users = {'user_name': 'Dominique'}
    shopping_list = ["pasta", "parmesan","eggs","bacon"]
    return render_template('index3.html', company_name='Nostos Genomics', slist = shopping_list)



if __name__ == "__main__"   :
    app.run(debug=True, port=5000)
