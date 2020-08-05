from flask import url_for, render_template, redirect, flash, request
from wtfforms import app
from wtfforms.forms import ContactForm, LoginForm, PrefOSForm
from wtfforms.models import Instance, Flavor

from wtfforms.provider.openstack import *
from wtfforms.db_load import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vm/start/<string:vm_uuid>')
def vm_start(vm_uuid):
    instance_start(vm_uuid)
    flash(f'Start... {vm_uuid}', 'success')
    return redirect(url_for('vm_list'))

@app.route('/vm/stop/<string:vm_uuid>')
def vm_stop(vm_uuid):
    instance_stop(vm_uuid)
    flash(f'Stop... {vm_uuid}', 'danger')
    return redirect(url_for('vm_list'))

@app.route('/vm/pause/<string:vm_uuid>')
def vm_pause(vm_uuid):
    flash(f'Pause... {vm_uuid}', 'warning')
    return redirect(url_for('vm_list'))

@app.route('/vm/console/<string:vm_uuid>')
def vm_console(vm_uuid):
    flash(f'Console redirect... {vm_uuid}', 'primary')
    return redirect(url_for('vm_list'))

@app.route('/vm/show/<string:vm_uuid>')
def vm_show(vm_uuid):
    instance = Instance.query.filter_by(uuid=vm_uuid).all()
    print(instance)
    return render_template('vm_show.html', instance=instance)

@app.route('/vm/list', methods=["GET","POST"])
def vm_list():
    instance = Instance.query.all()
    return render_template('vm_list.html', instance=instance)

@app.route('/login', methods=["GET","POST"])
def login_page():
    login = LoginForm()
    if request.method == "POST":
        #print(login.name.data)
        flash('You are now logged in', 'success')
        return redirect(url_for("home"))

    return render_template("login.html", form=login)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
    # if request.method == "POST":
        flash('Thank you for your message!', 'success')
        return redirect(url_for('home'))

    # if form.validate_on_submit():
    #     flash("Köszönjük, hogy üzenetet hagyott!")
    #     return redirect(url_for('home'))

    return render_template('contact.html', form=form)

@app.route('/pref-os', methods=["GET","POST"])
def openstack_preferences():
    pref_os = PrefOSForm()
    if pref_os.validate_on_submit():
        instance_load(instance_discover())
        flash('A virtuális gépek kiolvasása befejeződött!', 'success')
        return redirect(url_for('home'))
    return render_template('pref_openstack.html', form=pref_os)
