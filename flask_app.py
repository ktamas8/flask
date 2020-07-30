from flask import Flask, url_for, render_template
from config import Config
from forms import *

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def root(name=None):
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()
