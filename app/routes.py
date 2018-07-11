from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Ken'}
    title = 'Home'
    posts =[
        {
            'author':{'username':'Ken'},
            'blog':'Hello Yellow'
        },
        {
            'author':{'username':'Jack'},
            'blog':'Hello Bellow'
        }
    ]

    return render_template('index.html',user=user,title=title, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',form=form, title='Sign in')