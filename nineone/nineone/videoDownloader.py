from simplesqltool import SQLAccess
from items import NineoneItem

from SqlUtil import SQLAccess
import os
from subprocess import call
import youtube_dl

dbaccess = SQLAccess(host='yong-nuc', db='nineone')

ydl = youtube_dl.YoutubeDL()

class VideoDownloader:
	def __init__(self, host='yong-nuc', user='root', passwd='1234', db='nineone'):
		self._host = host
		self._user = user
		self._passwd = passwd
		self._db = db
		self.dao = SQLAccess(host=host, user=user, passwd=passwd, db=db)

	def getUndoneUrl(self, ct=20):
		with dbaccess.selectall('nine_videos') as vids:
			fresh = [(viewkey, url) for viewkey, url, title, done in vids if done is 0][:ct]
			print(fresh)
			return fresh

	def setVideoDone(self, viewkey):
		sql = 'update nine_videos set done = 1 where viewkey = {}'.format(viewkey)
		print(sql)
		with dbaccess.executeSql('update nine_videos set done = 1 where viewkey = "{}"'.format(viewkey)):
			pass

	def download(self, ct):
		vids = self.getUndoneUrl(ct)
		print(vids)
		for key, url in vids:
			os.chdir('/hdd/myporns/most_favor')
			with ydl:
				try:
					r=ydl.download([url])
					print(r)
					self.setVideoDone(key)
				except KeyboardInterrupt:
					raise
				except:
					print("Probably limit passed =====> \n\n")
			# print('the result of r is   ', r)
			# if r is 0:
			# 	print('limit probably exceed ===> ')
			# 	self.setVideoDone(key)
			# 	print(url, 'is down')


vd = VideoDownloader()
vd.download(20)




