import requests
import os.path

def download(url, filename):
	if os.path.isfile(filename):
		print('\n\nfile exists ==========> ', filename)
		return
	with open(filename, 'wb') as f:
		res = requests.get(url, stream=True)
		for block in res.iter_content(1024):
			f.write(block)

		print('file created ==> ', filename)
