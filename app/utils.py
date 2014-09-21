import requests
import simplejson

def github_post(url, payload, headers={}):
	default_headers = {
		'Accept': 'application/json'
	}
	headers.update(default_headers)

	print url
	print payload
	print headers
	r = requests.post(url, data=payload, headers=headers)
	print r.content
	result = simplejson.loads(r.content)

	if r.status_code == 200:
		return result
	else:
		if 'errors' in result:
			return result['errors']
		else:
			return None
