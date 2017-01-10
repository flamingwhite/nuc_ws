from filedownloader import download
from simplesqltool import SQLAccess
import os
import traceback

videoRootPath = '/hdd/wechat_web/Videos/insta_videos/'

access = SQLAccess(host='yong-nuc', user='root', passwd='1234', db='wind')

count, passed, downloaded = 0, 0, 0

with access.selectall('insta_videos') as videos:
	for vd in videos:
		try:
			print(vd, vd[0], vd[-1])
			user, id, url = vd[1], vd[0], vd[-1]

			filename = videoRootPath + user +'/'+ id+'.mp4'

			if not os.path.isdir(videoRootPath + user):
				os.mkdir(videoRootPath + user)

			if os.path.isfile(filename):
				passed += 1
			else:
				downloaded += 1
				download(url, filename)

			count += 1
			print('\n file size processed =====> ', count, ' passed ==> ', passed, '  downloaded ===> ', downloaded)
		except Exception as e:
			traceback.print_exc()
