import sqlite3
from flask import Flask
import scraper

DATABASE = '/tmp/word_dates.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def build_db():
	db = connect_db()
	try:
		db.execute('delete from word_dates')
	except:
		pass

	word_lines = open('static/5kdates.txt').readlines()
	for wl in word_lines: 
		parse_word_line(wl, db)

def parse_word_line(word_line, db):
	chopped = word_line.split('|')
	word_string = chopped[0]
	dates = chopped[1:]
	for date in dates:
		bits = date.split(':')
		word = {
			'word_string' 		: word_string,
			'part_of_speech' 	: bits[0],
			'earliest_use'		: bits[1]
		}
		make_db_entry(word, db)


def make_db_entry(word, db):
	word_string = word['word_string']
	part_of_speech = word['part_of_speech']
	earliest_use = word['earliest_use']

	print word
	try:
		db.execute('insert into word_dates (word_string, part_of_speech, earliest_use) values (?, ?, ?)', [unicode(word_string), unicode(part_of_speech), unicode(earliest_use)])
		db.commit()
	except Exception, e:
		print e

def query_db(req_string):
	db = connect_db()
	cursor = db.execute(req_string)
	return cursor.fetchall()

def get_words_by_word_string(word_string):
	return query_db('select * from word_dates where word_string = "' + word_string + '"')

def get_date_by_word_string_and_pos(word_string, pos):
	try:
		result = query_db('select earliest_use from word_dates where word_string = "' + word_string + '" and part_of_speech = "' + pos + '"')
		if result and len(result):
			return result[0][0]

	except Exception, e:
		try:
			print e
			word_line = word_string + scraper.get_file_line(word_string)
			print word_line
			# db = connect_db()
			# parse_word_line(word_line, db)
			# return query_db('select earliest_use from word_dates where word_string = "' + word_string + '" and part_of_speech = "' + pos + '"')[0][0]
		except Exception, e:
			print e

# print query_db('select earliest_use from word_dates where word_string = "the" and part_of_speech = "article"')[0]
