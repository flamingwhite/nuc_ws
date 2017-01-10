from .simplesqltool import SQLAccess
from .items import VideoItem

class VideoDao:
	def __init__(self, host='yong-nuc', user='root', passwd='1234', db='wind'):
		self._host = host
		self._user = user
		self._passwd = passwd
		self._db = db
		self.dao = SQLAccess(host=host, user=user, passwd=passwd, db=db)

	def videoNameExists(self, title):
		if len(title) < 10:
			return False
		with self.dao.query('select * from insta_videos where title = %s', (title,)) as exist:
			if len(exist) is 0:
				print('\nfound this title ==> ', title)
				return False
			else:
				print(title, 'already in db pass')
				return True

	def videoIdExists(self, id):
		with self.dao.query('select * from insta_videos where id = %s', (id,)) as exist:
			if len(exist) is 0:
				print('not found this id, i can insert ==> ', id)
				return False
			else:
				print(id, 'already in db pass=====> \n\n\n\n')
				return True

	def insertVideoToDb(self, item):
		try:
			if not self.videoIdExists(item.get('id')) and not self.videoNameExists(item.get('title')):
				with self.dao.executeSql("""insert into insta_videos (id, username, title, uploadtime, videourl) values(%s, %s, %s, %s, %s)""", (item.get('id'), item.get('username'), item.get('title'), item.get('uploadtime'), item.get('videourl'))):
					return True
			else:
				print('movide found, cannot insert')
				return False
		except Exception as e:
			print('error inserting', e)
			return False


