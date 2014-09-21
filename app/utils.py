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
	r = requests.post(url, data=payload)
	print r
	result = simplejson.loads(r.content)

	if r.status_code == 201:
		return result
	else:
		if 'errors' in result:
			return result['errors']
		else:
			return None
