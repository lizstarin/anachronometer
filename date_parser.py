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
		if self.date_string == None:
			return None
		elif self.__is_year():
			return int(self.date_string)
		else:
			return self.__parse()[0]

	def __find_latest(self):
		if self.date_string == None:
			return None
		elif self.__is_year():
			return int(self.date_string)
		else: 
			return self.__parse()[1]

	def __parse(self):
		p = re.compile('[\d]*[a-z]{2} [Cc]entury')
		q = re.compile('[Bb]efore')
		if p.search(self.date_string):
			century = int(re.search(r'\d+', self.date_string).group(0))
			if q.search(self.date_string):
				max_date = (century - 1) * 100
				return (None, max_date)
			else:
				max_date = century * 100
				min_date = max_date - 99
				return (min_date, max_date)
		else:
			return (None, None)

	def is_earlier_than(self, word_date):
		if self.latest < word_date.earliest:
			return True
		else:
			return False

	def is_later_than(self, word_date):
		if self.earliest > word_date.latest:
			return True
		else:
			return False

	def is_concurrent_with(self, word_date):
		if not self.is_earlier_than(word_date) and not word_date.is_earlier_than(self):
			return True
		else:
			return False
