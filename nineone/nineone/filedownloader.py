import requests
import os.path
import os
from subprocess import call

from videoDao import VideoDao

videoDao = VideoDao()

def download(url, filename):
	if os.path.isfile(filename):
		print('\n\nfile exists ==========> ', filename)
		return
	with open(filename, 'wb') as f:
		res = requests.get(url, stream=True)
		for block in res.iter_content(1024):
			f.write(block)

		print('file created ==> ', filename)


def download_url(url):
	os.chdir('/hdd/myporns/most_favor')
	call(['youtube-dl', url])


vids = videoDao.getUndoneUrl(20)
print(vids)
