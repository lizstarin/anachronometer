from bs4 import BeautifulSoup
import urllib2, re

f = open('static/5kdates.txt', 'w')

def find_date(definition_tag):
	try:
		date_card = definition_tag.find_next('div', {'class' : ['first-use-box', 'origin-box']})
		if 'first-use-box' in date_card.get('class'):
			return date_card.find('p').string
		else:
			return date_card.find(text = re.compile('First Known Use:')).split(': ')[1]
	except:
		raise

def get_file_line(word):
	file_line = ''

	url = 'http://www.merriam-webster.com/dictionary/' + word
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page, 'lxml')

	try:  
		base_word = soup.find('a', {'class' : 'ct-link'}).string # Is the word a tense or different case of some base word?
		return get_file_line(base_word)							 # So recurse by looking up the base word.

	except:
		definitions = soup.findAll('div', {'class' : 'word-and-pronunciation'})
		for d in definitions:
			try:
				part_of_speech = d.parent.parent.find('span', {'class' : 'main-attr'}).find('em').string
				try:
					date = find_date(d)
					file_line += '|' + str(part_of_speech) + ':' + str(date)
				except: 
					pass
			except:
				pass

	return file_line

def get_word_dates():
	words = [el.strip() for el in open('static/5k.txt').readlines()]
	for word in words:
		print word

		try:	
			file_line = word + get_file_line(word)
			f.write(file_line + '\n')
		except Exception, e:
			print e
