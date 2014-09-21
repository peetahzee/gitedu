from flask import Flask, session, render_template, request, redirect, url_for
import requests
import constants
import utils
from db import get_db
from models import User

app = Flask(__name__)
app.secret_key = constants.COOKIE_SECRET

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/oauth-authorize')
def oauth_authorize():
	token_result = utils.github_post('https://github.com/login/oauth/access_token', {
		'client_id': constants.CLIENT_ID,
		'client_secret': constants.CLIENT_SECRET,
		'code': request.values['code']
	})

	if token_result is None or 'access_token' not in token_result:
		return redirect(url_for('login'))
	
	session['logged_in'] = True
	session['github_token'] = token_result['access_token']
	return render_template('complete_reg.html')

@app.route('/oauth-authorize/confirm')
def confirm_reg():
	user_info = simplejson.load(gh_proxy('user'))

	db = get_db()
	user = User(name=request.values('name'),
		        email=request.values('email'),
		        username=user_info['login'])

	session.add(user)
	session.commit()


@app.route('/gh/<path:endpoint>')
def gh_proxy(endpoint):
	if session['logged_in']:
		headers = {
			'Accept': 'application/json',
			'Authorization': 'token ' + session['github_token']
		}
		r = requests.request(request.method, 
							 data=request.values.get('data', {}),
							 url='https://api.github.com/' + endpoint,
							 headers=headers)
		return r.content
	else:
		return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
