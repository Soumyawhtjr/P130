# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "SS" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name1 = "SS" # write your name
    age1 = "13" # write your age
    return render_template('father.html' , name = name1 , age = age1)
# define the route to mother webpage
@app.route("/mother")
def mother():
    name2 = "SS" # write your name
    age2 = "13" # write your age
    return render_template('mother.html' , name = name2 , age = age2)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name3 = "SS" # write your name
    age3 = "13" # write your age
    return render_template('friend.html' , name = name3 , age = age3)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
