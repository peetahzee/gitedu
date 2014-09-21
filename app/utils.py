import requests

def github_post(url, payload, headers={}):
	default_headers = {
		'Accept', 'application/json'
	}
	headers.update(default_headers)
	r = requests.post(url,
										data=simplejson.dumps(payload),
										headers=headers)
	result = simplejson.loads(r.content)

	if r.status_code == 201:
		return result
	else:
		if 'errors' in result:
			return result['errors']
		else:
			return None
