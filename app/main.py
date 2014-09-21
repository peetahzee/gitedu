from flask import Flask, session, render_template, request
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
	if 'access_token' in token_result:
		session['github_token'] = token_result['access_token']
	return render_template('complete_reg.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
