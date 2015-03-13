from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Jackie'}
    posts = [
        { 
            'author': {'nickname': 'Rachel'}, 
            'body': 'Beautiful day in Exeter, New Hampshire!' 
        },
        { 
            'author': {'nickname': 'Brooke'}, 
            'body': 'I just had the yummiest salad at this new restaurant.' 
        },
        { 
            'author': {'nickname': 'Daisy'}, 
            'body': 'Here are my tips for taking perfect Instagram shots!' 
        }
    ]
    return render_template('index.html',
    						title = 'Home',
    						user = user,
    						posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])