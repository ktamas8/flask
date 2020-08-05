from flask import url_for, render_template, redirect, flash, request
from wtfforms import app
from wtfforms.forms import ContactForm, LoginForm, PrefOS
from wtfforms.models import Instance, Flavor

from wtfforms.discover.openstack import *
from wtfforms.db_load import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vm')
def vm():
    # vm_list()
    # generate_vm_table_header(name, id)
    instance = Instance.query.all()
    return render_template('vm.html', instance=instance)

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

@app.route('/pref-os', methods=["GET","POST"])
def openstack_preferences():
    pref_os = PrefOS()
    if pref_os.validate_on_submit():
        instance_load(instance_discover())
        flash('A virtuális gépek kiolvasása befejeződött!', 'success')
        return redirect(url_for('home'))
    return render_template('pref_openstack.html', form=pref_os)
