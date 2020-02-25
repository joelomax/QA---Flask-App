from flask import render_template
from application import app

blogData = [
    {  
        "name": {"first":"John", "last":"Doe"},
        "title":"First Post",
        "content":"This is some blog data for Flask lectures"
    },
    {   
        "name": {"first":"Jane", "last":"Doe"},
        "title":"Second Post",
        "content":"This is even more blog data for Flask lectures"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home', posts=blogData)

