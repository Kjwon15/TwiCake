from flask import Flask, redirect, render_template, request, session, url_for
import sys
import tweepy
import time
from tweepy.auth import OAuthHandler
from tweepy.api import API

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#config of App
app.config.update(
    consumer_key='o7vgHO8hRGPl62L9xokp76Fan',
    consumer_secret='DuBOE39WluGJeRdUtz3sXAN7pjPr4mtoaRJYe5IueIRaeOejID'
)

class StreamListener(tweepy.streaming.StreamListener):
    tweet_id = None
    user_list = []

    def __init__(self, send_tweet_id):
        super(StreamListener, self).__init__()
        self.tweet_id = send_tweet_id 

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            retweeted_id =  status.retweeted_status.id
            retweeted_count = status.retweeted_status.retweet_count
            retweeted_user = status.author
            user_name = retweeted_user.screen_name
            if self.tweet_id == retweeted_id:
                print user_name
                self.user_list.append(user_name) 

    def on_error(self, status):
        print "can't get"

    def on_timeout(self):
        raise myExeption


class Rottery:
    getauth = None
    tweetid = None
    timer = None

    def __init__(self, oauth):
        self.getauth = oauth

    def Send(self, sendtweet, time):
        tweetobject = self.getapi.update_status(sendtweet)
        self.tweetid = tweetobject.id
        self.timer = time
        self.StreamingSerch()

    def StreamingSerch(self):
        listener = StreamListener(self.tweetid)
        stream = tweepy.Stream(self.getauth, listener, secure=True)
        stream.userstream(async=True)
        time.sleep(self.timer)
        stream.disconnect()



@app.route('/')
def my_render():
    if 'access_key' in session:
        return render_template('twicake.html', auth_url=url_for('auth'),
                access_status='login successful!')
    else:
        return render_template('twicake.html', auth_url=url_for('auth'),
                access_status='login not yet')


@app.route('/auth')
def auth():
    callback_url = url_for('get_auth', _external=True)
    auth = tweepy.OAuthHandler(app.config['consumer_key'],
            app.config['consumer_secret'], callback_url)
    try:
        redirect_url = auth.get_authorization_url()
        app.config['request_key'] = auth.request_token.key
        app.config['request_secret'] = auth.request_token.secret
        return redirect(redirect_url)
    except tweepy.TweepError as e:
        return render_template('error_auth.html',
                error_message=e.message), 401


@app.route('/', methods=['POST'])
def my_send_post():
    text = request.form['nickname']
    process_text = text.upper()
    return process_text


@app.route('/verify')
def get_auth():
    if 'oauth_verifier' in request.args:
        verifier = request.args['oauth_verifier']
        auth = tweepy.OAuthHandler(app.config['consumer_key'],
                app.config['consumer_secret'])
        auth.set_request_token(app.config['request_key'],
                app.config['request_secret'])
        try:
            auth.get_access_token(verifier)
            session['access_key'] = auth.access_token.key
            session['access_secret'] = auth.access_token.secret
            session['request_key'] = app.config['request_key']
            session['request_secret'] = app.config['request_secret']
        except tweepy.TweepError as e:
            return render_template('error_auth.html',
                    error_message=e.message), 401
        return redirect(url_for('my_render'))

    else:
        return redirect(url_for('my_render'))
