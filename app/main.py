from flask import Flask, session, render_template, request, redirect, url_for
import constants
import utils

app = Flask(__name__)
app.secret_key = constants.COOKIE_SECRET

@app.route('/')
def hello_world():
    return 'Hello World!'


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

@app.route('/gh/<endpoint>')
def gh_proxy(verb, endpoint):
	if session['logged_in']:
		print request.values
		default_headers = {
			'Accept': 'application/json',
			'Authorization': 'token ' + session['github_token']
		}
		r = requests.request(request.method, endpoint, data=request.values,
												   headers=headers)
		return r.body
	else:
		return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
