from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
application = app


@app.route('/')
def my_render():
    url = url_for('twitter')
    return render_template('twicake.html', redirect_url=url)


@app.route('/', methods=['POST'])
def my_send_post():
    text = request.form['nickname']
    process_text = text.upper()
    return process_text


@app.route('/twitter')
def twitter():
    return redirect('http://twitter.com')
