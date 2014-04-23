from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def my_render():
    return render_template('twicake.html')


@app.route('/', methods=['POST'])
def my_send_post():
    text = request.form['nickname']
    process_text = text.upper()
    return process_text


@app.route('/twitter')
def twitter():
    return redirect('http://twitter.com')
