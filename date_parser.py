import re

class WordDate(object):

	def __init__(self, date_string):
		self.date_string = date_string
		self.earliest = self.__find_earliest()
		self.latest = self.__find_latest()

	def __is_year(self):
		p = re.compile('^\d+$')
		return True if p.match(self.date_string) else False

	def __find_earliest(self):
		if self.__is_year():
			return int(self.date_string)
		else:
			return self.__parse()[0]

	def __find_latest(self):
		if self.__is_year():
			return int(self.date_string)
		else: 
			return self.__parse()[1]

	def __parse(self):
		p = re.compile('[\d]*[a-z]{2} [Cc]entury')
		q = re.compile('[Bb]efore')
		if p.search(self.date_string):
			if q.search(self.date_string):
				max_date = (int(self.date_string.split()[1][0:2]) - 1) * 100
				return (None, max_date)
			else:
				max_date = int(self.date_string.split()[0][0:2]) * 100
				min_date = max_date - 99
				return (min_date, max_date)
		else:
			return (None, None)

	def is_earlier_than(word_date):
		return 'blah'

d = WordDate('before 12th century')
print d.latest