from .simplesqltool import SQLAccess
from .items import NineoneItem

from .SqlUtil import SQLAccess

dbaccess = SQLAccess(host='yont-nuc', db='nineone')

class VideoDao:
	def __init__(self, host='yong-nuc', user='root', passwd='1234', db='nineone'):
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
		with self.dao.query('select * from nine_videos where viewkey = %s', (id,)) as exist:
			if len(exist) is 0:
				print('not found this id, i can insert ==> ', id)
				return False
			else:
				print(id, 'already in db pass=====> \n\n\n\n')
				return True

	def getUndoneUrl(self, ct=20):
		with dbaccess.selectall('nine_videos') as vids:
			fresh = [(viewkey, url) for viewkey, url, title, done in vids if done is 0][:ct]
			print(fresh)
			return fresh

	def setVideoDone(self, viewkey):
		with dbaccess.executeSql('update nine_videos set done = 1 where id = {}'.format(viewkey)):
			pass

	def insertVideoToDb(self, item):
		try:
			if not self.videoIdExists(item.get('viewkey')):
				with self.dao.executeSql("""insert into nine_videos (viewkey, url, title, done) values(%s, %s, %s, %s)""", (item.get('viewkey'), item.get('url'), item.get('title'), item.get('done'))):
					return True
			else:
				print('movide found, cannot insert')
				return False
		except Exception as e:
			print('error inserting', e)
			return False


