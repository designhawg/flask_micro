from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    posts = [
      {
        'author': { 'nickname': 'John' },
        'body': 'Beautiful day in Portland!'
      },
      {
        'author': { 'nickname': 'Chris' },
        'body': 'Woo Pig Sooie!'
      },
      {
        'author': { 'nickname': 'Riley' },
        'body': 'I love Frozen'
      },
      {
        'author': { 'nickname': 'Karen' },
        'body': 'I don\'t wanna be here'
      }
    ]

    return render_template("index.html",
      title = "homer",
      user = user,
      posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
      flash('Login requested for OpenID = "' + form.openid.data + '", remember_me ' + str(form.remember_me.data))
      return redirect('/index')

    return render_template("login.html",
      title = "Sign In",
      form = form,
      providers = app.config['OPENID_PROVIDERS'])
