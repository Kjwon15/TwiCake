from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
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

#app.debug = True
#app.run(host='0.0.0.0', port=9999)
