from flask import url_for, render_template, redirect, flash, request
from wtfforms import app
from wtfforms.forms import ContactForm, LoginForm, PrefOSForm, VMControlForm
from wtfforms.models import Instance, Flavor

from wtfforms.discover.openstack import *
from wtfforms.db_load import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vm/start/<string:vm_uuid>')
def vm_start(vm_uuid):
    flash(f'Start... {vm_uuid}', 'success')
    return redirect(url_for('vm_list2'))

@app.route('/vm/stop/<string:vm_uuid>')
def vm_stop(vm_uuid):
    flash(f'Stop... {vm_uuid}', 'danger')
    return redirect(url_for('vm_list2'))

@app.route('/vm/pause/<string:vm_uuid>')
def vm_pause(vm_uuid):
    flash(f'Pause... {vm_uuid}', 'warning')
    return redirect(url_for('vm_list2'))

@app.route('/vm/console/<string:vm_uuid>')
def vm_console(vm_uuid):
    flash(f'Console redirect... {vm_uuid}', 'primary')
    return redirect(url_for('vm_list2'))

@app.route('/vm/show/<string:vm_uuid>')
def vm_show(vm_uuid):
    flash('Instance info', 'secondary')
    return redirect(url_for('vm_list2'))

# @app.route('/vm/<string:vm_uuid>')
# def vm_show(vm_uuid):
#
#     instance = Instance.query.filter_by(uuid=vm_uuid).all()
#     print(instance)
#     return render_template('vm_show.html', instance=instance)

@app.route('/vm', methods=["GET","POST"])
def vm_list():
    vmcontrol = VMControlForm()
    instance = Instance.query.all()

    if vmcontrol.start.data:
        #print(instance.uuid.data)
        vm_start()
    elif vmcontrol.stop.data:
        vm_stop()
    elif vmcontrol.pause.data:
        vm_pause()
    elif vmcontrol.console.data:
        vm_console(instance)
    elif vmcontrol.show.data:
        print(instance)
        vm_info()

    return render_template('vm_list.html', instance=instance, vmcontrol=vmcontrol)

@app.route('/vm2', methods=["GET","POST"])
def vm_list2():
    vmcontrol = VMControlForm()
    instance = Instance.query.all()

    if vmcontrol.start.data:
        vm_start()
    elif vmcontrol.stop.data:
        vm_stop()
    elif vmcontrol.pause.data:
        vm_pause()
    elif vmcontrol.console.data:
        vm_console()
    elif vmcontrol.show.data:
        vm_show()

    return render_template('vm_list2.html', instance=instance, vmcontrol=vmcontrol)

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
