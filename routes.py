from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Michael is so awesome at coding!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Poopity-scoop'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
