from flask import Flask, render_template, flash
#from content_management import Content

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/dashboard/')
def dashboard():
    flash("flash test!!!!")
    flash("fladfasdfsaassh test!!!!")
    flash("asdfas asfsafs!!!!")
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

#https://pythonprogramming.net/flash-flask-tutorial/
