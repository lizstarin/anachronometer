from bs4 import BeautifulSoup
import urllib2, re

f = open('static/testdates.txt', 'w')

def get_word_dates():
	words = open('static/test.txt').readlines()
	return [get_word_date(word.strip()) for word in words]

def find_date(definition_tag):
	try:
		date_card = definition_tag.find_next('div', {'class' : ['first-use-box', 'origin-box']}) #.find('p').string
		if 'first-use-box' in date_card.get('class'):
			return date_card.find('p').string
		else:
			return date_card.find(text = re.compile('First Known Use:')).split(': ')[1]
	except:
		pass

def find_definition_info(definition_tag):
	try:
		part_of_speech = definition_tag.find_next('div', {'class' : 'word-attributes'}).find('span', {'class' : 'main-attr'}).find('em').string
		date = find_date(definition_tag)
		if date: 
			return '|' + str(part_of_speech) + ':' + str(date)
		else:
			return ''
	except:
		base_word = definition_tag.find_next('p', {'class' : 'definition-inner-item'}).find('a').string
		get_word_date(base_word)

def get_word_date(word):
	print word

	try:
		file_line = word

		url = 'http://www.merriam-webster.com/dictionary/' + word
		html_page = urllib2.urlopen(url)
		soup = BeautifulSoup(html_page, 'lxml')
		definitions = soup.findAll('div', {'class' : 'word-and-pronunciation'})

		for d in definitions:
			try:
				file_line += find_definition_info(d)
			except:
				pass

		f.write(file_line + '\n')

	except Exception, e:
		print e


get_word_dates()