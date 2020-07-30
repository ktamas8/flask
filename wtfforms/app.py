from flask import Flask, url_for, render_template, redirect, flash, request
from forms import ContactForm, LoginForm
from config import Config

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login_page():
    login = LoginForm()
    if request.method == "POST":
        flash('You are now logged in', 'success')
        return redirect(url_for("home"))

    return render_template("login.html", form=login)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
    # if request.method == "POST":
        flash('Köszönjük, hogy üzenetet hagyott!', 'success')
        return redirect(url_for('home'))

    # if form.validate_on_submit():
    #     flash("Köszönjük, hogy üzenetet hagyott!")
    #     return redirect(url_for('home'))

    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
