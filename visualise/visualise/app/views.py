from flask import render_template, redirect, url_for, request
from app import app


@app.route('/visualise', methods=['GET', 'POST'])
def visualise():
    index = "RDSB"
    dynamic = False
    if request.method == 'POST':
        index = request.form['index']
        dynamic = True
    return render_template('visualise.html',
                           index=index,
                           dynamic=dynamic)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return redirect(url_for('visualise'))
